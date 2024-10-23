# Клас "Текст"
class Text:
    def __init__(self, content, language):
        self.content = content  # зміст тексту
        self.language = language  # мова тексту

    def create_text(self, content, language):
        self.content = content
        self.language = language

    def display_text(self):
        return f"Текст: '{self.content}' (Мова: {self.language})"

# Клас "Шрифт"
class Font:
    def __init__(self, font_name, size, bold, italic, underline):
        self.font_name = font_name  # назва шрифту
        self.size = size  # кегль
        self.bold = bold  # напівгрубий
        self.italic = italic  # нахилений
        self.underline = underline  # підкреслений

    def create_font(self, font_name, size, bold, italic, underline):
        self.font_name = font_name
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def display_font(self):
        return (f"Шрифт: {self.font_name}, Кегль: {self.size}, "
                f"Напівгрубий: {'Так' if self.bold else 'Ні'}, "
                f"Нахилений: {'Так' if self.italic else 'Ні'}, "
                f"Підкреслений: {'Так' if self.underline else 'Ні'}")

# Клас "ТекстовийНадпис" (успадковує від Text та Font)
class TextLabel(Text, Font):
    def __init__(self, content, language, font_name, size, bold, italic, underline, color):
        # Виклик ініціалізаторів батьківських класів
        Text.__init__(self, content, language)
        Font.__init__(self, font_name, size, bold, italic, underline)
        self.color = color  # колір текстового надпису

    def create_text_label(self, content, language, font_name, size, bold, italic, underline, color):
        # Викликаємо методи для встановлення властивостей з батьківських класів
        self.create_text(content, language)
        self.create_font(font_name, size, bold, italic, underline)
        self.color = color

    def display_text_label(self):
        text_info = self.display_text()
        font_info = self.display_font()
        return f"{text_info}\n{font_info}\nКолір: {self.color}"

# Приклад використання
text_label = TextLabel("Привіт, світ!", "Українська", "Arial", 14, True, False, True, "Червоний")

# Виведення інформації про текстовий надпис
print(text_label.display_text_label())
