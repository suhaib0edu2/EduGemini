# تطبيق EduGemini

class EduGemini:
    def __init__(self):
        self.content = []

    def add_content(self, text):
        self.content.append(text)

    def get_content(self):
        return self.content

    def interactive_questions(self):
        # هنا يمكن إضافة منطق الأسئلة التفاعلية
        pass

if __name__ == '__main__':
    app = EduGemini()
    # مثال على إضافة محتوى
    app.add_content("هذا نص درس تجريبي.")
    print(app.get_content())
