class usa():
    def capital(self):
        print("WashingtonDC is the capital of usa")
    def language(self):
        print("Amarican English is the pyrimre language")
class uk():
    def capital(self):
        print("Londan is the capital of uk")
    def language(self):
        print("Britsh English is the pyrimre language")
ob_usa=usa()
ob_uk=uk()
for country in (ob_usa,ob_uk):
    country.capital()
    country.language()
