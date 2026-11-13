---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.FareyNumeratorWanted.fareyNumeratorCount, MathlibExt.NumberTheory.FareyNumeratorWanted.farey_between_count, MathlibExt.NumberTheory.FareyNumeratorWanted.fareyNumeratorCount_formula
statement: formalized
---

# Farey fractions with a given numerator

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-fractions-with-a-given-numerator/index.html).

## Number of Farey fractions with a given numerator

For natural numbers $n$ and $h$, $N_n(h)$
is the number of integers $b$ with $h \le b \le n$ and $\gcd(h, b) = 1$; for $h \ge 1$ this is
the number of fractions with numerator $h$ in the Farey sequence of order $n$.

Formalized by `MathlibExt.NumberTheory.FareyNumeratorWanted.fareyNumeratorCount`, a definition declared in [WantedExt/NumberTheory/FareyNumeratorWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FareyNumeratorWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-fractions-with-a-given-numerator/index.html#farey-numerator-count).

## Farey fractions with equal numerators between consecutive unit fractions

Let $k$, $n$
and $h$ be natural numbers with $k > 1$, $h \ge 1$ and $n \ge kh - 1$, and let $\varphi$ be Euler's
totient function. The number of integers $b$ with $1 \le b \le n$, $\gcd(h, b) = 1$ and
$1/k < h/b \le 1/(k-1)$ is $\varphi(h)$. If moreover $h > 2$, then twice the number of integers
$b$ with $1 \le b \le n$, $\gcd(h, b) = 1$ and $1/k < h/b < 2/(2k-1)$ is $\varphi(h)$.

Equivalently, the Farey sequence of order $n$ has exactly $\varphi(h)$ fractions with numerator
$h$ in the interval $(1/k, 1/(k-1)]$, and for $h > 2$ exactly $\varphi(h)/2$ in the interval
$(1/k, 2/(2k-1))$.

## Sources

- Rogelio Tomás García, "Farey Fractions with Equal Numerators and the Rank of Unit Fractions", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.FareyNumeratorWanted.farey_between_count` is written with `theorem_wanted` in [WantedExt/NumberTheory/FareyNumeratorWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FareyNumeratorWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-fractions-with-a-given-numerator/index.html#farey-between-count).

## Formula for the number of Farey fractions with a given numerator

Let $h$ and $n$ be
natural numbers with $0 < h < n$, and let $N_n(h)$ be the number of integers $b$ with
$h \le b \le n$ and $\gcd(h, b) = 1$ (the number of fractions with numerator $h$ in the Farey
sequence of order $n$). Then

$$
N_n(h) = \frac{n \varphi(h)}{h} - \sum_{d \mid h} \mu(d) \frac{n \bmod d}{d} -
\varphi(h) + \delta_{1h},
$$

where $\varphi$ is Euler's totient function, $\mu$ is the Möbius function, the sum runs over the
positive divisors $d$ of $h$, $(n \bmod d)/d$ is the fractional part of $n/d$, and $\delta_{1h}$ is
$1$ if $h = 1$ and $0$ otherwise.

## Sources

- Rogelio Tomás García, "Farey Fractions with Equal Numerators and the Rank of Unit Fractions", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.FareyNumeratorWanted.fareyNumeratorCount_formula` is written with `theorem_wanted` in [WantedExt/NumberTheory/FareyNumeratorWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FareyNumeratorWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-fractions-with-a-given-numerator/index.html#farey-numerator-count-formula).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Farey fractions with a given numerator](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-fractions-with-a-given-numerator/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-fractions-with-a-given-numerator)
