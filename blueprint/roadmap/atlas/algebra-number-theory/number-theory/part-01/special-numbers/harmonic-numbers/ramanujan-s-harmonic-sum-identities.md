---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry1.ramanujan_part1_ch2_entry1_general, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry1.ramanujan_part1_ch2_entry1, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry1Corollary.ramanujan_part1_ch2_entry1_corollary, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry2.ramanujan_part1_ch2_entry2_general, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry2.ramanujan_part1_ch2_entry2, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry2Corollary.ramanujan_part1_ch2_entry2_corollary, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry4.ramanujan_part1_ch2_entry4_general, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry4.ramanujan_part1_ch2_entry4
statement: formalized
proof: formalized
---

# Ramanujan's harmonic sum identities

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html).

## Ramanujan's identity for $\sum_{k=1}^{n} 1/(n+k)$, including $n = 0$

For every natural
number $n$,

$$\sum_{k=1}^{n} \frac{1}{n+k} = \frac{n}{2n+1} + \sum_{k=1}^{n} \frac{1}{(2k)^3 - 2k}.$$

This is Ramanujan's Entry 1 of Chapter 2 without the hypothesis $n \ge 1$; at $n = 0$ both sides
are $0$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry1.ramanujan_part1_ch2_entry1_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry1.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry1.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry1-general).

## Ramanujan's identity for $\sum_{k=1}^{n} 1/(n+k)$

For every positive integer $n$,

$$\sum_{k=1}^{n} \frac{1}{n+k} = \frac{n}{2n+1} + \sum_{k=1}^{n} \frac{1}{(2k)^3 - 2k}.$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 1, formula (1.1), printed p. 25 / PDF p. 35.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry1.ramanujan_part1_ch2_entry1`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry1.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry1.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry1).

## Ramanujan's series $\sum_{k \ge 1} 1/((2k)^3 - 2k) = \log 2 - 1/2$

The series

$$\sum_{k=1}^{\infty} \frac{1}{(2k)^3 - 2k}$$

converges, and its sum is $\log 2 - \frac{1}{2}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, corollary to Entry 1, printed p. 26 / PDF p. 36.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry1Corollary.ramanujan_part1_ch2_entry1_corollary`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry1Corollary.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry1Corollary.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry1-corollary).

## Ramanujan's identity for $\sum_{k=1}^{2n+1} 1/(n+k)$, including $n = 0$

For every
natural number $n$,

$$\sum_{k=1}^{2n+1} \frac{1}{n+k} = 1 + 2 \sum_{k=1}^{n} \frac{1}{(3k)^3 - 3k}.$$

This is Ramanujan's Entry 2 of Chapter 2 without the hypothesis $n \ge 1$; at $n = 0$ both sides
are $1$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry2.ramanujan_part1_ch2_entry2_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry2.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry2.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry2-general).

## Ramanujan's identity for $\sum_{k=1}^{2n+1} 1/(n+k)$

For every positive integer $n$,

$$\sum_{k=1}^{2n+1} \frac{1}{n+k} = 1 + 2 \sum_{k=1}^{n} \frac{1}{(3k)^3 - 3k}.$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 2, formula (2.1), printed p. 27 / PDF p. 37.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry2.ramanujan_part1_ch2_entry2`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry2.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry2.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry2).

## Ramanujan's series $\sum_{k \ge 1} 1/((3k)^3 - 3k) = (\log 3 - 1)/2$

The series

$$\sum_{k=1}^{\infty} \frac{1}{(3k)^3 - 3k}$$

converges, and its sum is $\frac{\log 3 - 1}{2}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, corollary to Entry 2, printed p. 27 / PDF p. 37.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry2Corollary.ramanujan_part1_ch2_entry2_corollary`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry2Corollary.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry2Corollary.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry2-corollary).

## Ramanujan's sum identity for $1/((4k)^3 - 4k)$, including $n = 0$

For every natural
number $n$,

$$
\sum_{k=1}^{n} \frac{1}{n+k} + \sum_{k=0}^{n} \frac{1}{2n+2k+1} =
1 + 2 \sum_{k=1}^{n} \frac{1}{(4k)^3 - 4k}.
$$

At $n = 0$ both sides equal $1$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry4.ramanujan_part1_ch2_entry4_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry4.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry4.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry4-general).

## Ramanujan's sum identity for $1/((4k)^3 - 4k)$

For every positive integer $n$,

$$
\sum_{k=1}^{n} \frac{1}{n+k} + \sum_{k=0}^{n} \frac{1}{2n+2k+1} =
1 + 2 \sum_{k=1}^{n} \frac{1}{(4k)^3 - 4k}.
$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 4, formula (4.1), printed p. 28 / PDF p. 38. It follows from `ramanujan_part1_ch2_entry4_general`, which extends it to `n = 0`; the hypothesis `hn` is unused and keeps the source's shape.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry4.ramanujan_part1_ch2_entry4`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry4.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry4.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry4).

## Alternating form of Ramanujan's identity for $1/((4k)^3 - 4k)$, including $n = 0$

For
every natural number $n$,

$$
1 + 2 \sum_{k=1}^{n} \frac{1}{(4k)^3 - 4k} =
\sum_{k=1}^{4n+1} \frac{(-1)^{k+1}}{k} + \frac{1}{2} \sum_{k=1}^{2n} \frac{(-1)^{k+1}}{k}.
$$

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry4AlternatingForm.ramanujan_part1_ch2_entry4_alternating_form_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry4AlternatingForm.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry4AlternatingForm.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry4-alternating-f).

## Alternating form of Ramanujan's sum identity for $1/((4k)^3 - 4k)$

For every positive
integer $n$,

$$
1 + 2 \sum_{k=1}^{n} \frac{1}{(4k)^3 - 4k} =
\sum_{k=1}^{4n+1} \frac{(-1)^{k+1}}{k} + \frac{1}{2} \sum_{k=1}^{2n} \frac{(-1)^{k+1}}{k}.
$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 4, formula (4.1), printed p. 28 / PDF p. 38.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry4AlternatingForm.ramanujan_part1_ch2_entry4_alternating_form`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry4AlternatingForm.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry4AlternatingForm.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry4-alternating-f-2).

## Ramanujan's series for $\frac{3}{2}\log 2 - 1$

The numbers $\frac{2}{(4k)^3 - 4k}$ for
$k = 1, 2, 3, \dots$ are summable with sum $\frac{3}{2}\log 2 - 1$, where $\log$ is the natural
logarithm.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, corollary to Entry 4, printed p. 29 / PDF p. 39.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry4Corollary.ramanujan_part1_ch2_entry4_corollary`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry4Corollary.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry4Corollary.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry4-corollary).

## Ramanujan's sum identity for $1/((6k)^3 - 6k)$, including $n = 0$

For every natural
number $n$,

$$
1 + 2 \sum_{k=1}^{n} \frac{1}{(6k)^3 - 6k} =
\frac{2}{3} \sum_{k=1}^{n} \frac{1}{n+k} + \sum_{k=0}^{2n} \frac{1}{2n+2k+1}.
$$

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry5.ramanujan_part1_ch2_entry5_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry5.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry5.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry5-general).

## Ramanujan's sum identity for $1/((6k)^3 - 6k)$

For every positive integer $n$,

$$
1 + 2 \sum_{k=1}^{n} \frac{1}{(6k)^3 - 6k} =
\frac{2}{3} \sum_{k=1}^{n} \frac{1}{n+k} + \sum_{k=0}^{2n} \frac{1}{2n+2k+1}.
$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 5, formula (5.1), printed p. 29 / PDF p. 39.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry5.ramanujan_part1_ch2_entry5`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry5.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry5.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry5).

## Ramanujan's series for $\frac{1}{2}\log 3 + \frac{1}{3}\log 4 - 1$

The numbers
$\frac{2}{(6k)^3 - 6k}$ for $k = 1, 2, 3, \dots$ are summable with sum
$\frac{1}{2}\log 3 + \frac{1}{3}\log 4 - 1$, where $\log$ is the natural logarithm.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, corollary to Entry 5, printed p. 30 / PDF p. 40.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry5Corollary.ramanujan_part1_ch2_entry5_corollary`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry5Corollary.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry5Corollary.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry5-corollary).

## The tripling sequence of Ramanujan's Entry 6

For natural numbers $n$ and $k$, let
$A(n, k) = 3^k n + (3^k - 1)/2$, a natural number. It is the sequence with $A(n, 0) = n$ and
$A(n, k + 1) = 3A(n, k) + 1$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry6.A`, a definition declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#a).

## Starting value of the tripling sequence

For every natural number $n$, the tripling
sequence $A(n, k)$ of Entry 6 satisfies $A(n, 0) = n$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry6.A_zero`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#a-zero).

## Recurrence of the tripling sequence

For all natural numbers $n$ and $k$, the tripling
sequence $A(n, k)$ of Entry 6 satisfies $A(n, k + 1) = 3A(n, k) + 1$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry6.A_succ`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#a-succ).

## The tripling sequence never drops below its starting value

For all natural numbers
$n$ and $k$, the tripling sequence $A(n, k)$ of Entry 6 satisfies $n \le A(n, k)$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry6.A_ge`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#a-ge).

## Ramanujan's harmonic sum identity (Entry 6, general form)

For all natural numbers $n$
and $r$, the following identity holds in $\mathbb{Q}$:

$$
\sum_{j=n+1}^{A(n, r)} \frac{1}{j} = r + 2 \sum_{k=0}^{r-1} (r - k)
\sum_{j=a_k}^{A(n, k)} \frac{1}{(3j)^3 - 3j},
$$

where $A(n, k)$ is the tripling sequence of Entry 6, $a_0 = 1$ and $a_k = A(n, k - 1) + 1$ for
$k \ge 1$, and a sum over an empty range is $0$. For $r = 0$ both sides are $0$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry6.ramanujan_part1_ch2_entry6_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry6-general).

## Ramanujan's harmonic sum identity (Entry 6)

For all natural numbers $n$ and $r$ with
$r > 0$, the following identity holds in $\mathbb{Q}$:

$$
\sum_{j=n+1}^{A(n, r)} \frac{1}{j} = r + 2 \sum_{k=0}^{r-1} (r - k)
\sum_{j=a_k}^{A(n, k)} \frac{1}{(3j)^3 - 3j},
$$

where $A(n, k)$ is the tripling sequence of Entry 6 (with $A(n, 0) = n$ and
$A(n, k + 1) = 3A(n, k) + 1$), $a_0 = 1$ and $a_k = A(n, k - 1) + 1$ for $k \ge 1$, and a sum
over an empty range is $0$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 6, printed p. 33 / PDF p. 43. It follows from `ramanujan_part1_ch2_entry6_general`; the hypothesis `hr` is unused and keeps the source's shape.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry6.ramanujan_part1_ch2_entry6`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry6).

## The tripling sequence starting at zero

For a natural number $k$, let
$A(k) = (3^k - 1)/2 = 1 + 3 + \cdots + 3^{k-1}$, a natural number with $A(0) = 0$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry6Corollary.A`, a definition declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6Corollary.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6Corollary.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#a-2).

## Twice the tripling sequence plus one is a power of three

For every natural number
$k$, $2A(k) + 1 = 3^k$, where $A(k) = (3^k - 1)/2$; in particular the division by $2$ in the
definition of $A(k)$ is exact.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry6Corollary.A_two_mul_add_one`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6Corollary.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6Corollary.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#a-two-mul-add-one).

## Ramanujan's harmonic sum identity (corollary to Entry 6, general form)

For every
natural number $r$, the following identity holds in $\mathbb{Q}$:

$$
\sum_{j=1}^{A(r)} \frac{1}{j} = r + 2 \sum_{k=1}^{r-1} (r - k)
\sum_{j=A(k-1)+1}^{A(k)} \frac{1}{(3j)^3 - 3j},
$$

where $A(k) = (3^k - 1)/2$ and a sum over an empty range is $0$. For $r = 0$ both sides are $0$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry6Corollary.ramanujan_part1_ch2_entry6_corollary_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6Corollary.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6Corollary.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry6-corollary-gen).

## Ramanujan's harmonic sum identity (corollary to Entry 6)

For every natural number
$r > 0$, the following identity holds in $\mathbb{Q}$:

$$
\sum_{j=1}^{A(r)} \frac{1}{j} = r + 2 \sum_{k=1}^{r-1} (r - k)
\sum_{j=A(k-1)+1}^{A(k)} \frac{1}{(3j)^3 - 3j},
$$

where $A(k) = (3^k - 1)/2 = 1 + 3 + \cdots + 3^{k-1}$ and a sum over an empty range is $0$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, corollary to Entry 6, printed p. 33 / PDF p. 43.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry6Corollary.ramanujan_part1_ch2_entry6_corollary`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6Corollary.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry6Corollary.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html#ramanujan-part1-ch2-entry6-corollary).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramanujan's harmonic sum identities](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-harmonic-sum-identities)
