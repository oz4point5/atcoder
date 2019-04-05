def array_count(arr):
    arr_target = [[]]
    cnt = 1
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            cnt += 1
        else:
            arr_target.append([arr[i-1],cnt])
            cnt = 1
    arr_target.append([arr[len(arr)-1],cnt])
    del arr_target[0]
    return arr_target

def digit_list(num):
    num = str(num)
    num = list(num)
    num = list(map(int,num))
    return num

def list_digit(arr):
    arr = map(str,arr)
    arr = "".join(arr)
    arr = int(arr)
    return arr

def binary_search(l, value):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        #ここの条件式を変更する
        if l[mid] == value:
            return True
        elif l[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
    def root(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)

def lcm(a, b):
    "gcd関数を必要とする"
    return (a * b) // gcd(a,b)

def sieve_of_eratosthenes(target):
    dest = int(math.sqrt(target))
    target_list = list(range(2, target + 1))
    prime_list = []
    while True:
        num_min = min(target_list)
        if num_min >= dest:
            prime_list.extend(target_list)
            break
        prime_list.append(num_min)
        i = 0
        while True:
            if i >= len(target_list):
                break
            elif target_list[i] % num_min == 0:
                target_list.pop(i)
            i += 1
    return prime_list

class Dijkstra(object):
    def dijkstra(self, adj, start, goal=None):
        '''
        ダイクストラアルゴリズムによる最短経路を求めるメソッド
        入力
        adj: adj[i][j]の値が頂点iから頂点jまでの距離(頂点iから頂点jに枝がない場合，値はfloat('inf'))となるような2次元リスト(正方行列)
        start: 始点のID
        goal: オプション引数．終点のID
        出力
        goalを引数に持つ場合，startからgoalまでの最短経路を格納したリストを返す
        持たない場合は，startから各頂点までの最短距離を格納したリストを返す
        >>> d = Dijkstra()
        >>> d.dijkstra([[float('inf'), 2, 4, float('inf'), float('inf')], [2, float('inf'), 3, 5, float('inf')], [4, 3, float('inf'), 1, 4], [float('inf'), 5, 1, float('inf'), 3], [float('inf'), float('inf'), 4, 3, float('inf')]], 0)
        [0, 2, 4, 5, 8] # 例えば，始点0から頂点3までの最短距離は5となる
        >>> d.dijkstra([[float('inf'), 2, 4, float('inf'), float('inf')], [2, float('inf'), 3, 5, float('inf')], [4, 3, float('inf'), 1, 4], [float('inf'), 5, 1, float('inf'), 3], [float('inf'), float('inf'), 4, 3, float('inf')]], 0, goal=4)
        [0, 2, 4] # 頂点0から頂点4までの最短経路は0 -> 2 -> 4となる
        '''
        num = len(adj)
        dist = [float('inf') for i in range(num)]
        prev = [float('inf') for i in range(num)]

        dist[start] = 0
        q = []
        heapq.heappush(q, (0, start))

        while len(q) != 0:
            prov_cost, src = heapq.heappop(q)

            if dist[src] < prov_cost:
                continue

            for dest in range(num):
                cost = adj[src][dest]
                if cost != float('inf') and dist[dest] > dist[src] + cost:
                    dist[dest] = dist[src] + cost
                    heapq.heappush(q, (dist[dest], dest))
                    prev[dest] = src

        if goal is not None:
            return self.get_path(goal, prev)
        else:
            return dist

    def get_path(self, goal, prev):
        '''
        始点startから終点goalまでの最短経路を求める
        '''
        path = [goal]
        dest = goal

        while prev[dest] != float('inf'):
            path.append(prev[dest])
            dest = prev[dest]

        return list(reversed(path))

def list_intersection(a,b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c.append(a[i])
                a[i] = "_"
                b[j] = "&"
    return c

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct

#bit全探索
n = 3
arr = [0] * n
for i in range(2 ** n):
    for j in range(n):
        if((1&i>>j) == 1):
            arr[j] = 1
        else:
            arr[j] = 0
    #ここに処理
    print(arr)

#深さ優先探索
def search(x, y):
    if x < 0 or x >= w or y < 0 or y >= h:
        return False
    if c[y][x] == "#":
        return False
    if check[y][x] == 1:
        return False
    if c[y][x] == "g":
        return True
    check[y][x] = 1

    if search(x+1, y):
        return True
    if search(x-1, y):
        return True
    if search(x, y+1):
        return True
    if search(x, y-1):
        return True
    return False
