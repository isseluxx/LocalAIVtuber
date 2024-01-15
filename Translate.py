from pluginLoader import plugin_loader
from pluginInterface import TranslationPluginInterface
import gradio as gr
import utils

selected_provider = None


def create_ui():
    category_name = plugin_loader.interface_to_category[TranslationPluginInterface]
    ProviderList, ProviderMap = utils.pluginToNameMap(
        plugin_loader.plugins[category_name])
    default_provider_name = ProviderList[0] if ProviderList else None
    global selected_provider
    selected_provider = ProviderMap[default_provider_name]
    load_provider()
    with gr.Tab("Translate"):
        # translation provider selection
        gr.Dropdown(
            choices=ProviderList,
            value=default_provider_name,
            type="value",
            label="Translation provider: ",
            info="Select the translation provider",
            interactive=True)
        # translation UI
        gr.Interface(
            fn=selected_provider.translate,
            inputs=[gr.Textbox(label="Original Text", lines=3)],
            outputs=[gr.Textbox(label="Translated Text", lines=3)],
            allow_flagging="never",
            examples=["My name is Wolfgang and I live in Berlin",
                      "VHave you ever kept goldfish as pets? They're very cute."]
        )


def load_provider():
    global selected_provider
    if issubclass(type(selected_provider), TranslationPluginInterface):
        print("Loading Translation Module...")
        selected_provider.init()
