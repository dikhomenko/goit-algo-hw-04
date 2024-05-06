## Порівняння трьох алгоритмів сортування: Insertion, Merge та Timsort

Insertion Sort: 3.6469105238000337 seconds
Merge Sort: 0.04250196700086235 seconds
Timsort (sorted): 0.0019379406003281474 seconds

Insertion Sort: 3.792513938600314 seconds
Merge Sort: 0.06433960380090867 seconds
Timsort (sorted): 0.0019869486000970936 seconds

Insertion Sort: 3.7387164994004705 seconds
Merge Sort: 0.035535101599816696 seconds
Timsort (sorted): 0.0019289946001663338 seconds

Insertion Sort: 3.4896002297995437 seconds
Merge Sort: 0.03561433560098522 seconds
Timsort (sorted): 0.0021826366006280295 seconds

Insertion Sort: 3.424044345199218 seconds
Merge Sort: 0.03564206560040475 seconds
Timsort (sorted): 0.0026513823999266607 seconds


![alt text](https://github.com/dikhomenko/goit-algo-hw-04/blob/f2605ada4defe93534c8b9b18abce885d706369c/img/chart.png)

Оцінки складності алгоритмів:

- Складність сортування вставками - O(n^2), працює добре на невеликих масивах, але зростає дуже швидко зі збільшенням розміру вхідного масиву.
- Складність сортування злиттям - O(n log n), що робить його більш ефективним для великих масивів порівняно з сортуванням вставками.
- Timsort поєднує обидва алгоритми, використовуючи сортування злиттям для обробки великих підмасивів та сортування вставками для малих підмасивів, що робить його ефективним на різних розмірах масивів.

### Отже, саме поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим, особливо на великих масивах даних. Це пояснює чому програмісти у більшості випадків використовують вбудовані алгоритми сортування, які базуються на Timsort, замість написання власних реалізацій.