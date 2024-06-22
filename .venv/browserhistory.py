from collections import deque

class browserhistory:
    def __init__(self):
        self.backward_history = deque()
        self.forward_history = deque()
        self.current_page = "Google Search Page"

    def go_backward(self):
        if self.isEmpty(self.backward_history):
            print("No more backward pages")
            return
        self.forward_history.appendleft(self.current_page)
        self.current_page = self.backward_history.pop()


    def go_foward(self):
        if isEmpty(self.forward_history):
            print("There are no forward pages")
            return
        self.backward_history.append(self.current_page)
        self.current_page = self.forward_history.popleft()

    def search_new_page(self,current_page):
        self.backward_history.append(self.current_page)
        self.forward_history.clear()
        self.current_page = current_page

    def isEmpty(self,history):
        if len(history) != 0:
            return False
        return True
if __name__ == "__main__":
    chrome_browser = browserhistory()
    chrome_browser.search_new_page("github.com")

    chrome_browser.go_backward()
    print(chrome_browser.current_page)
    print(chrome_browser.forward_history)
    print(chrome_browser.backward_history)