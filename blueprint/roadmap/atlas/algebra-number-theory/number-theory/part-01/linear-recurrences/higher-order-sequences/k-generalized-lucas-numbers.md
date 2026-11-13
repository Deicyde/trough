---
declaration: section
origin: cited
lean: Nat.kGeneralizedLucas, Nat.kGeneralizedLucas_zero, Nat.kGeneralizedLucas_one, Nat.kGeneralizedLucas_neg_eq_zero, Nat.kGeneralizedLucas_lower_zero, Nat.kGeneralizedLucas_recurrence, MetaMathlibExt.nStepLucasList, MetaMathlibExt.nStepLucas
statement: formalized
proof: formalized
---

# k-generalized Lucas numbers

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-lucas-numbers/index.html).

## $k$-generalized Lucas numbers

For a natural number $k \ge 2$, the $k$-generalized Lucas
numbers $L^{(k)}_n$ are the natural numbers indexed by the integers $n \ge 2 - k$ given by
$L^{(k)}_n = 0$ for $2 - k \le n \le -1$, $L^{(k)}_0 = 2$, $L^{(k)}_1 = 1$, and
$L^{(k)}_n = L^{(k)}_{n-1} + L^{(k)}_{n-2} + \dots + L^{(k)}_{n-k}$ for every integer $n \ge 2$. No
value is assigned at indices below $2 - k$.

Formalized by `Nat.kGeneralizedLucas`, a definition declared in [MathlibExt/NumberTheory/GeneralizedLucas.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedLucas.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-lucas-numbers/index.html#k-generalized-lucas).

## $k$-generalized Lucas numbers at index zero

For every natural number $k \ge 2$, the
$k$-generalized Lucas number $L^{(k)}_0$ equals $2$.

Formalized by `Nat.kGeneralizedLucas_zero`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedLucas.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedLucas.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-lucas-numbers/index.html#k-generalized-lucas-zero).

## $k$-generalized Lucas numbers at index one

For every natural number $k \ge 2$, the
$k$-generalized Lucas number $L^{(k)}_1$ equals $1$.

Formalized by `Nat.kGeneralizedLucas_one`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedLucas.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedLucas.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-lucas-numbers/index.html#k-generalized-lucas-one).

## $k$-generalized Lucas numbers vanish at negative indices

For every natural number
$k \ge 3$ and every integer $n$ with $2 - k \le n \le -1$, the $k$-generalized Lucas number
$L^{(k)}_n$ equals $0$.

Formalized by `Nat.kGeneralizedLucas_neg_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedLucas.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedLucas.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-lucas-numbers/index.html#k-generalized-lucas-neg-eq-zero).

## $k$-generalized Lucas numbers at the lowest index

For every natural number $k \ge 3$,
the $k$-generalized Lucas number $L^{(k)}_{2-k}$ equals $0$.

Formalized by `Nat.kGeneralizedLucas_lower_zero`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedLucas.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedLucas.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-lucas-numbers/index.html#k-generalized-lucas-lower-zero).

## Recurrence for the $k$-generalized Lucas numbers

For every natural number $k \ge 2$ and
every integer $n \ge 2$, the $k$-generalized Lucas numbers satisfy
$L^{(k)}_n = \sum_{i=0}^{k-1} L^{(k)}_{n-k+i}$, that is, $L^{(k)}_n$ is the sum
$L^{(k)}_{n-1} + \dots + L^{(k)}_{n-k}$ of the $k$ preceding values.

Formalized by `Nat.kGeneralizedLucas_recurrence`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedLucas.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedLucas.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-lucas-numbers/index.html#k-generalized-lucas-recurrence).

## Finite prefixes of the n-step Lucas numbers

For natural numbers $n$ and $m$, this is the
list $[L^{(n)}_1, \dots, L^{(n)}_m]$ of length $m$ (empty for $m = 0$), where
$L^{(n)}_k = 2^k - 1$ for $1 \le k \le n$ and $L^{(n)}_k$ is the sum of the $n$ preceding terms
for $k \ge n + 1$. For $n = 0$ every term is $0$.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL14/Saito/saito22.tex>.

Formalized by `MetaMathlibExt.nStepLucasList`, a definition declared in [MathlibExt/NumberTheory/NStepLucasSequence.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NStepLucasSequence.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-lucas-numbers/index.html#n-step-lucas-list).

## n-step Lucas numbers

For natural numbers $n \ge 1$ and $m$, the $n$-step Lucas number
$L^{(n)}_m$ is defined by $L^{(n)}_0 = 0$, $L^{(n)}_m = 2^m - 1$ for $1 \le m \le n$, and
$L^{(n)}_m = \sum_{i=1}^{n} L^{(n)}_{m-i}$ for $m \ge n + 1$. For $n = 0$ we set
$L^{(0)}_m = 0$ for every $m$.

The source defines $L^{(n)}_m$ only for $m \ge 1$; the value $L^{(n)}_0 = 0$ is a convention.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL14/Saito/saito22.tex>.

Formalized by `MetaMathlibExt.nStepLucas`, a definition declared in [MathlibExt/NumberTheory/NStepLucasSequence.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NStepLucasSequence.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-lucas-numbers/index.html#n-step-lucas).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: k-generalized Lucas numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-lucas-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-lucas-numbers)
