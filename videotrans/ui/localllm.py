# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from videotrans.configure import config
from videotrans.util import tools


class Ui_localllmform(object):
    def setupUi(self, localllmform):
        self.has_done = False
        localllmform.setObjectName("localllmform")
        localllmform.setWindowModality(QtCore.Qt.NonModal)
        localllmform.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(localllmform.sizePolicy().hasHeightForWidth())
        localllmform.setSizePolicy(sizePolicy)
        localllmform.setMaximumSize(QtCore.QSize(600, 600))

        v1=QtWidgets.QVBoxLayout(localllmform)

        h1=QtWidgets.QHBoxLayout()
        h2=QtWidgets.QHBoxLayout()
        h3=QtWidgets.QHBoxLayout()
        h4=QtWidgets.QHBoxLayout()

        self.label_0 = QtWidgets.QLabel()
        self.label_0.setText(
            '兼容OpenAI接口的本地大模型在此使用，例如ollama，api地址通常以 /v1 结尾' if config.defaulelang == 'zh' else 'AIs compatible with the ChatGPT Local LLM also used here')

        v1.addWidget(self.label_0)

        self.label = QtWidgets.QLabel(localllmform)
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setObjectName("label")
        self.localllm_api = QtWidgets.QLineEdit(localllmform)
        self.localllm_api.setMinimumSize(QtCore.QSize(0, 35))
        self.localllm_api.setObjectName("localllm_api")
        h1.addWidget(self.label)
        h1.addWidget(self.localllm_api)
        v1.addLayout(h1)


        self.label_2 = QtWidgets.QLabel(localllmform)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.localllm_key = QtWidgets.QLineEdit(localllmform)
        self.localllm_key.setMinimumSize(QtCore.QSize(0, 35))
        self.localllm_key.setObjectName("localllm_key")
        h2.addWidget(self.label_2)
        h2.addWidget(self.localllm_key)
        v1.addLayout(h2)

        self.label_3 = QtWidgets.QLabel(localllmform)
        self.label_3.setObjectName("label_3")
        self.localllm_model = QtWidgets.QComboBox(localllmform)
        self.localllm_model.setMinimumSize(QtCore.QSize(0, 35))
        self.localllm_model.setObjectName("localllm_model")
        h3.addWidget(self.label_3)
        h3.addWidget(self.localllm_model)
        v1.addLayout(h3)

        self.label_allmodels = QtWidgets.QLabel(localllmform)
        self.label_allmodels.setObjectName("label_allmodels")
        self.label_allmodels.setText(
            '填写所有可用模型，以英文逗号分隔，填写后可在上方选择' if config.defaulelang == 'zh' else 'Fill in all available models, separated by commas. After filling in, you can select them above')
        v1.addWidget(self.label_allmodels)
        self.edit_allmodels = QtWidgets.QPlainTextEdit(localllmform)
        self.edit_allmodels.setObjectName("edit_allmodels")
        v1.addWidget(self.edit_allmodels)


        self.label_4 = QtWidgets.QLabel(localllmform)
        self.label_4.setObjectName("label_4")
        v1.addWidget(self.label_4)

        self.localllm_template = QtWidgets.QPlainTextEdit(localllmform)
        self.localllm_template.setObjectName("localllm_template")
        v1.addWidget(self.localllm_template)

        self.set_localllm = QtWidgets.QPushButton(localllmform)

        self.set_localllm.setMinimumSize(QtCore.QSize(0, 35))
        self.set_localllm.setObjectName("set_localllm")

        self.test_localllm = QtWidgets.QPushButton(localllmform)
        self.test_localllm.setMinimumSize(QtCore.QSize(0, 30))
        self.test_localllm.setObjectName("test_localllm")
        help_btn = QtWidgets.QPushButton()
        help_btn.setMinimumSize(QtCore.QSize(0, 35))
        help_btn.setStyleSheet("background-color: rgba(255, 255, 255,0)")
        help_btn.setObjectName("help_btn")
        help_btn.setCursor(Qt.PointingHandCursor)
        help_btn.setText("查看填写教程" if config.defaulelang == 'zh' else "Fill out the tutorial")
        help_btn.clicked.connect(lambda: tools.open_url(url='https://pyvideotrans.com/localllm'))
        h4.addWidget(self.set_localllm)
        h4.addWidget(self.test_localllm)
        h4.addWidget(help_btn)
        v1.addLayout(h4)

        self.retranslateUi(localllmform)
        QtCore.QMetaObject.connectSlotsByName(localllmform)

    def retranslateUi(self, localllmform):
        localllmform.setWindowTitle("Local LLM API" if config.defaulelang != 'zh' else '兼容AI及本地大模型')
        self.label_3.setText('选择模型' if config.defaulelang == 'zh' else "Model")
        self.localllm_template.setPlaceholderText("prompt")
        self.label_4.setText(
            "{lang}代表目标语言名称，不要删除。" if config.defaulelang == 'zh' else "{lang} represents the target language name, do not delete it.")
        self.set_localllm.setText('保存' if config.defaulelang == 'zh' else "Save")
        self.test_localllm.setText('测试..' if config.defaulelang == 'zh' else "Test..")
        self.localllm_api.setPlaceholderText(
            '大模型Api接口地址，不自动加/v1,如有需要请手动加' if config.defaulelang == 'zh' else 'Local LLM API url')
        self.localllm_key.setPlaceholderText("Secret key")
        self.localllm_key.setToolTip("若未设置留空即可" if config.defaulelang == 'zh' else 'If not remain empty')
        self.label.setText("API接口地址" if config.defaulelang == 'zh' else 'API url')
        self.label_2.setText("SK")
