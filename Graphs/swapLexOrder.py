def swapLexOrder(string, pairs):
    graph = {}
    for x, y in pairs:
        graph.setdefault(x-1, []).append(y-1)
        graph.setdefault(y-1, []).append(x-1)
    visited = set()
    pairs = []
    for k, v in graph.items():
        if k in visited:
            continue
        stack = [k]
        pair = []
        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            pair.append(curr)
            stack += graph[curr]
        pairs.append(pair)
    
    largest = string
    for pair in pairs:
        curr = list(largest)
        chars = []
        for idx in pair:
            chars.append(curr[idx])
        chars.sort(reverse=True)
        pair.sort()
        for idx, char in zip(pair, chars):
            curr[idx] = char
        largest = max(largest, "".join(curr))
    return largest