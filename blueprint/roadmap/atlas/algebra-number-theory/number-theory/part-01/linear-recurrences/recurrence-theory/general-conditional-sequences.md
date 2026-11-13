---
declaration: section
origin: cited
lean: MetaMathlibExt.decimationCoeff, MetaMathlibExt.decimationCoeff_zero, MetaMathlibExt.decimationCoeff_one, MetaMathlibExt.decimation_generating_function, MetaMathlibExt.decimation_binet
statement: formalized
---

# General conditional sequences

5 results, 3 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/general-conditional-sequences/index.html).

## Decimation coefficients

Let $(A_j)_{j \ge 0}$ and $(s_n)_{n \ge 0}$ be sequences in a
commutative ring and let $m$, $r$ be natural numbers. For natural numbers $l$ and $i$, the
decimation coefficient is

$$v_l^{(i)} = s_{lr+i} - \sum_{j\lt l} A_{m-1-j} s_{(l-1-j)r+i},$$

an index $m-1-j$ that would be negative being read as $0$. For $l \le m$ this is
$v_l^{(i)} = s_{lr+i} - A_{m-1} s_{(l-1)r+i} - \cdots - A_{m-l} s_i$.

## Sources

- Emre Güday and Murat Sahin, *Linear Recurrence Relations Satisfied by the General Conditional Sequences*, INTEGERS 26 (2026), Article A5, Theorem 1.

Formalized by `MetaMathlibExt.decimationCoeff`, a definition declared in [WantedExt/NumberTheory/GeneralConditionalSequenceWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralConditionalSequenceWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/general-conditional-sequences/index.html#decimation-coeff).

## Zeroth decimation coefficient

For sequences $(A_j)_{j \ge 0}$ and $(s_n)_{n \ge 0}$ in
a commutative ring and natural numbers $m$, $r$, $i$, the decimation coefficient $v_0^{(i)}$
equals $s_i$.

## Sources

- Emre Güday and Murat Sahin, *Linear Recurrence Relations Satisfied by the General Conditional Sequences*, INTEGERS 26 (2026), Article A5, Theorem 1.

Formalized by `MetaMathlibExt.decimationCoeff_zero`, a theorem declared in [WantedExt/NumberTheory/GeneralConditionalSequenceWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralConditionalSequenceWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/general-conditional-sequences/index.html#decimation-coeff-zero).

## First decimation coefficient

For sequences $(A_j)_{j \ge 0}$ and $(s_n)_{n \ge 0}$ in a
commutative ring and natural numbers $m$, $r$, $i$, the decimation coefficient $v_1^{(i)}$
equals $s_{r+i} - A_{m-1} s_i$, where $A_{m-1}$ is read as $A_0$ when $m = 0$.

## Sources

- Emre Güday and Murat Sahin, *Linear Recurrence Relations Satisfied by the General Conditional Sequences*, INTEGERS 26 (2026), Article A5, Theorem 1.

Formalized by `MetaMathlibExt.decimationCoeff_one`, a theorem declared in [WantedExt/NumberTheory/GeneralConditionalSequenceWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralConditionalSequenceWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/general-conditional-sequences/index.html#decimation-coeff-one).

## Generating function of a decimated linear recurrence

Let $R$ be a commutative ring,
let $m$ and $r$ be natural numbers, and let $(A_j)_{j \ge 0}$ and $(s_n)_{n \ge 0}$ be
sequences in $R$ such that $s_{n+mr} = \sum_{j\lt m} A_j s_{n+jr}$ for all $n \ge 0$. Then, in
the ring $R[[x]]$ of formal power series,

$$
\Bigl(\sum_{n \ge 0} s_n x^n\Bigr)\Bigl(1 - \sum_{j\lt m} A_j x^{(m-j)r}\Bigr) =
\sum_{i\lt r} \sum_{l\lt m} v_l^{(i)} x^{lr+i},
$$

where $v_l^{(i)} = s_{lr+i} - \sum_{j\lt l} A_{m-1-j} s_{(l-1-j)r+i}$ are the decimation
coefficients. The second factor on the left is the denominator
$1 - A_{m-1} x^r - A_{m-2} x^{2r} - \cdots - A_0 x^{mr}$ of the generating function.

The printed denominator ends in $- A_1 x^{mr} - A_0$ and the printed hypothesis names
Relation (1); this is the reading of the paper's derivation and of its Example 2 ($m = 2$:
$1 - A_1 x^r - A_0 x^{2r}$).

## Sources

- Emre Güday and Murat Sahin, *Linear Recurrence Relations Satisfied by the General Conditional Sequences*, INTEGERS 26 (2026), Article A5, Theorem 1.

Stated but not proved: `MetaMathlibExt.decimation_generating_function` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralConditionalSequenceWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralConditionalSequenceWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/general-conditional-sequences/index.html#decimation-generating-function).

## Binet formula for decimated linear recurrences

Let $m$ and $r$ be natural numbers and
let $(A_j)_{j \ge 0}$ and $(s_n)_{n \ge 0}$ be sequences of complex numbers such that
$s_{n+mr} = \sum_{j\lt m} A_j s_{n+jr}$ for all $n \ge 0$. Let $f(x) = x^m - \sum_{j\lt m} A_j x^j$
and let $\alpha_1, \ldots, \alpha_m$ be pairwise distinct roots of $f$ in $\mathbb{C}$. Then
for every $n \ge 0$

$$
s_n = \sum_{l\lt m} v_l^{(n \bmod r)}
\sum_{t=1}^{m} \frac{\alpha_t^{m-1-l+\lfloor n/r \rfloor}}{f'(\alpha_t)},
$$

where $v_l^{(i)} = s_{lr+i} - \sum_{j\lt l} A_{m-1-j} s_{(l-1-j)r+i}$ are the decimation
coefficients. For $r = 0$ the formula is read with $n \bmod 0 = n$ and
$\lfloor n/0 \rfloor = 0$.

## Sources

- Emre Güday and Murat Sahin, *Linear Recurrence Relations Satisfied by the General Conditional Sequences*, INTEGERS 26 (2026), Article A5, Theorem 2.

Stated but not proved: `MetaMathlibExt.decimation_binet` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralConditionalSequenceWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralConditionalSequenceWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/general-conditional-sequences/index.html#decimation-binet).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: General conditional sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/general-conditional-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/recurrence-theory/general-conditional-sequences)
