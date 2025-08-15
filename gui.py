import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QTextEdit,
)
import io
import xv2tool


class Xeno2GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Xeno2 Save Tool")
        self.setGeometry(100, 100, 600, 400)

        self.file_path = None
        self.is_decrypted = False

        layout = QVBoxLayout()

        self.label = QLabel("No file selected")
        layout.addWidget(self.label)

        self.select_button = QPushButton("Select File")
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        self.process_button = QPushButton("Load a Save first")
        self.process_button.clicked.connect(self.process_file)
        self.process_button.setEnabled(False)
        layout.addWidget(self.process_button)

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        layout.addWidget(self.log_box)

        self.setLayout(layout)
        self.apply_dark_theme()

    def apply_dark_theme(self):
        dark_style = """
        QWidget {
            background-color: #2b2b2b;
            color: #f0f0f0;
            font-family: Consolas, Courier, monospace;
            font-size: 12pt;
        }
        QPushButton {
            background-color: #3c3f41;
            border: 1px solid #5c5c5c;
            padding: 5px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #505357;
        }
        QTextEdit {
            background-color: #1e1e1e;
            color: #f0f0f0;
            border: 1px solid #5c5c5c;
        }
        QLabel {
            font-weight: bold;
        }
        """
        self.setStyleSheet(dark_style)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Save File")
        if file_path:
            self.file_path = file_path
            self.label.setText(f"Selected: {file_path}")
            self.process_button.setEnabled(True)

            try:
                with open(file_path, "rb") as f:
                    header = f.read(4)
                expected_header = bytes.fromhex("23 53 41 56")
                self.is_decrypted = header == expected_header
            except Exception:
                self.is_decrypted = False

            self.process_button.setText("Load a Save")

    def process_file(self):
        if not self.file_path:
            return

        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        try:
            xv2tool.calc_checksum(self.file_path)
        except Exception as e:
            print(f"Error: {e}")

        sys.stdout = old_stdout
        self.log_box.setPlainText(buffer.getvalue())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Xeno2GUI()
    window.show()
    sys.exit(app.exec())
