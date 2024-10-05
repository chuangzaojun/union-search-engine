import jieba

class KeywordTable:
    def __init__(self):
        self.table  = {
            "创造" : {"创造君"},
            "君" : {"创造君"}
        }

    def add(self, keyword: str, content: str):
        if keyword in self.table:
            self.table[keyword].add(content)
        else:
            self.table[keyword] = {content}

    def search(self, keyword: str) -> list:
        if keyword in self.table:
            return list(self.table[keyword])
        else:
            return []


class Engine:
    def __init__(self):
        self.keyword_table = KeywordTable()

    def add(self, content: str):
        keywords = jieba.cut_for_search(content)
        for keyword in keywords:
            self.keyword_table.add(keyword, content)

    def search(self, content: str) -> set:
        keywords = jieba.cut_for_search(content)
        results = set()
        for keyword in keywords:
            results.update(self.keyword_table.search(keyword))
        return results