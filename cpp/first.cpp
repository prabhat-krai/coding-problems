#include <iostream>
#include <cmath>

using namespace std;

class Book {
	private:
		int pages;
	public:
		string name;
		string author;
		Book(string Aname, string Aauthor, int Apages){
			name = Aname;
			author = Aauthor;
			setPages(Apages);
		}

		string isThick(){
			if(pages > 200){
				return "true";
			} 
			return "false";
		}

		void setPages(int aPages){
			if(aPages > 100 && aPages < 500){
				pages = aPages;
			} else {
				cout << "The page count was invalid";
			}
		}

		int getPages(){
			return pages;
		}
};

int main()
{
	Book book1("Physics", "HCV", 400);

	cout << book1.getPages() << endl;
	cout << book1.isThick();
	return 0;
}
