---
declaration: section
origin: cited
lean: MetaMathlibExt.genocchiNumberViaBernoulli, MetaMathlibExt.medianGenocchiOdd, MetaMathlibExt.medianGenocchiOdd_divisibility
statement: formalized
proof: formalized
---

# Median Genocchi numbers

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-genocchi-numbers/index.html).

## Genocchi numbers via Bernoulli numbers

For a natural number $n$, the Genocchi number $G_n$
is the rational number $G_n = 2(1 - 2^n) B_n$, where $B_n$ is the $n$-th Bernoulli number with the
convention $B_1 = -\tfrac{1}{2}$.

Formalized by `MetaMathlibExt.genocchiNumberViaBernoulli`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MedianGenocchiNumber.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MedianGenocchiNumber.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-genocchi-numbers/index.html#genocchi-number-via-bernoulli).

## Odd-indexed median Genocchi numbers

For a natural number $m$, let $B_m$ be the $m$-th
Bernoulli number and $G_m = 2(1 - 2^m) B_m$ the $m$-th Genocchi number. For a natural number $n$,
the median Genocchi number $H_{2n+1}$ is the rational number defined by $H_1 = 1$ and, for
$n \ge 1$,

$$H_{2n+1} = \sum_{k=0}^{\lfloor (n-1)/2 \rfloor} \binom{n}{2k+1} G_{2n-2k}.$$

These values carry signs: $H_3 = -1$ and $H_5 = 2$.

Formalized by `MetaMathlibExt.medianGenocchiOdd`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MedianGenocchiNumber.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MedianGenocchiNumber.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-genocchi-numbers/index.html#median-genocchi-odd).

## Divisibility of the median Genocchi numbers

Let $H_{2m+1}$ denote the odd-indexed median
Genocchi values, with the signs given by their defining sum, so that $H_5 = 2$, $H_7 = -8$ and
$H_9 = 56$. For every natural number $n \ge 1$ there is an integer $z$ with $H_{2n+3} = 2^n z$,
and $z \equiv 1 \pmod 6$ if $n$ is odd, while $z \equiv 4 \pmod 6$ if $n$ is even.

Proof: The antisymmetry of the Euler–Seidel matrix of the Genocchi numbers writes $H_{2n+3}$ as
an alternating sum of Legendre–Stirling numbers times $k!\,(k+1)!$. Pulling a power of two out of
each term gives the factor $2^n$; in the remaining sum every term from the fourth on is divisible
by $6$, which gives the residue. The divisibility and residue arguments are Chen's, applied to
this finite sum instead of his continued fraction.

## Sources

- Kwang-Wu Chen, *An Interesting Lemma for Regular C-fractions*, Journal of Integer Sequences 6 (2003), Article 03.4.8: <https://cs.uwaterloo.ca/journals/JIS/VOL6/Chen/chen50.tex>.

Formalized by `MetaMathlibExt.medianGenocchiOdd_divisibility`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MedianGenocchiDivisibility.lean, line 798](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MedianGenocchiDivisibility.lean#L798). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-genocchi-numbers/index.html#median-genocchi-odd-divisibility).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Median Genocchi numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-genocchi-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-genocchi-numbers)
