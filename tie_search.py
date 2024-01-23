class TrieNode:
    def __init__(self):
        self.Children = {}
        self.Is_Terminal = False
        self.Value = None


def TrieInsert(x, key, value):
    for i in range(len(key)):
        if key[i] not in x.Children:
            x.Children[key[i]] = TrieNode()
        x = x.Children[key[i]]

    x.Value = value
    x.Is_Terminal = True


def TrieFind(x, key):
    i = 0
    while i < len(key):
        if key[i] not in x.Children:
            return None
        x = x.Children[key[i]]
        i += 1

    return x


def TrieDelete(x, key):
    if key == "":
        if x.Is_Terminal:
            x.Is_Terminal = False
            x.Value = None

        # 자식 노드가 있는지 확인하고, 없으면 해당 노드를 삭제
        for child_key in x.Children:
            if x.Children[child_key] is not None:
                return x

        return None

    if key[0] in x.Children:
        x.Children[key[0]] = TrieDelete(x.Children[key[0]], key[1:])

    return x


# 예제를 위해 Trie를 만들어보겠습니다.
trie_root = TrieNode()

# 값 추가
TrieInsert(trie_root, "apple", "fruit")
TrieInsert(trie_root, "app", "application")

# 값 찾기
search_key = "apple"
result_node = TrieFind(trie_root, search_key)

if result_node is not None:
    print(f"Value for key '{search_key}': {result_node.Value}")
    print(f"Is Terminal: {result_node.Is_Terminal}")
else:
    print(f"Key '{search_key}' not found in the Trie.")

# 값 삭제
delete_key = "app"
TrieDelete(trie_root, delete_key)

# 삭제 후 Trie 확인
result_node = TrieFind(trie_root, delete_key)

if result_node is not None:
    print(f"Value for key '{delete_key}': {result_node.Value}")
    print(f"Is Terminal: {result_node.Is_Terminal}")
else:
    print(f"Key '{delete_key}' not found in the Trie.")