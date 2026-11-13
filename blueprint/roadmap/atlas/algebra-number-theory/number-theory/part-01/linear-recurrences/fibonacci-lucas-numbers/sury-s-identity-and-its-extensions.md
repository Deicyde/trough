---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.fibAtInt, MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.lucasAtInt, MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.second_order_recurrence_initial_one_sury_sum, MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.second_order_recurrence_offset_sury_sum, MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.fib_step_sury_sum, MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.lucas_step_sury_sum, MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.fib_step_offset_sury_sum, MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.lucas_step_offset_sury_fib_sum
statement: formalized
---

# Sury's identity and its extensions

8 results, 2 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/sury-s-identity-and-its-extensions/index.html).

## Fibonacci numbers extended to negative indices

For an integer $n$, the Fibonacci number
$F_n$ as a rational number, where $F_0 = 0$, $F_1 = 1$, $F_{m+2} = F_{m+1} + F_m$ for natural
numbers $m$, and $F_{-m} = (-1)^{m+1} F_m$ for natural numbers $m$.

Formalized by `MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.fibAtInt`, an abbreviation declared in [WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/sury-s-identity-and-its-extensions/index.html#fib-at-int).

## Lucas numbers at integer indices

For an integer $n$, the Lucas number $L_n$ as a
rational number, where $L_0 = 2$, $L_1 = 1$, $L_{m+2} = L_{m+1} + L_m$ for natural numbers $m$,
and $L_{-m} = (-1)^m L_m$ for natural numbers $m$.

Formalized by `MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.lucasAtInt`, a definition declared in [WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/sury-s-identity-and-its-extensions/index.html#lucas-at-int).

## Sury's identity for a second-order recurrence starting at 1

Let $c_1, c_2$ be rational
numbers with $c_2 \neq 0$, and let $(A_n)_{n \ge 0}$ be a sequence of rational numbers with
$A_0 = 1$ and $A_{n+2} = c_1 A_{n+1} + c_2 A_n$ for all $n \ge 0$. Put $t = c_1 - A_1$ and
assume $t \neq 0$. Then for every natural number $n$,

$$A_{n+2} - A_1 A_{n+1} = (A_2 - A_1^2) \sum_{i=0}^{n} t^{n-i} A_i.$$

## Sources

- Gregory Dresden and Xiaoya Gao, "Further Extensions of Sury's Identity", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.second_order_recurrence_initial_one_sury_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/sury-s-identity-and-its-extensions/index.html#second-order-recurrence-initial-one-sury).

## Offset form of Sury's identity for a second-order recurrence

Let $c_1, c_2$ be rational
numbers with $c_2 \neq 0$, and let $(X_n)_{n \in \mathbb{Z}}$ be a sequence of rational numbers
with $X_{n+2} = c_1 X_{n+1} + c_2 X_n$ for all integers $n$. Let $k$ be an integer with
$X_k \neq 0$ and $X_{k-1} \neq 0$. Then for every natural number $n$,

$$X_0 X_{n+2} - X_1 X_{n+1} = \frac{X_0 X_2 - X_1^2}{X_k}
\sum_{i=0}^{n} \left(\frac{-c_2 X_{k-1}}{X_k}\right)^{n-i} X_{i+k}.$$

The offset $k$ may be negative; requiring the recurrence at every integer index encodes the
paper's backward extension of the sequence, which uses $c_2 \neq 0$.

## Sources

- Gregory Dresden and Xiaoya Gao, "Further Extensions of Sury's Identity", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.second_order_recurrence_offset_sury_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/sury-s-identity-and-its-extensions/index.html#second-order-recurrence-offset-sury-sum).

## Step extension of Sury's identity for Fibonacci numbers

Let $F_n$ and $L_n$ be the
Fibonacci and Lucas numbers at integer indices. For all natural numbers $j \ge 1$ and $n$,

$$L_j^{n+1} F_{j(n-1)} + (-1)^{j(n+1)} F_{2j} = \sum_{i=0}^{n} (-1)^{j(n+i)} L_j^i F_{ji}.$$

When $n = 0$ the index $j(n-1) = -j$ is negative, so $F_{-j} = (-1)^{j+1} F_j$ enters.

## Sources

- Gregory Dresden and Xiaoya Gao, "Further Extensions of Sury's Identity", Theorem 3.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.fib_step_sury_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/sury-s-identity-and-its-extensions/index.html#fib-step-sury-sum).

## Step extension of Sury's identity for Lucas numbers

Let $F_n$ and $L_n$ be the Fibonacci
and Lucas numbers at integer indices. For all natural numbers $j \ge 1$ and $n$, in the rational
numbers,

$$2 \left(\frac{L_j}{2}\right)^{n+1} \frac{F_{jn}}{F_j} + 2 (-1)^{jn} =
\sum_{i=0}^{n} (-1)^{j(n+i)} \left(\frac{L_j}{2}\right)^i L_{ji}.$$

## Sources

- Gregory Dresden and Xiaoya Gao, "Further Extensions of Sury's Identity", Theorem 4.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.lucas_step_sury_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/sury-s-identity-and-its-extensions/index.html#lucas-step-sury-sum).

## Offset step extension of Sury's identity, Fibonacci form

Let $F_n$ be the Fibonacci
numbers at integer indices. For all natural numbers $j$ and $n$ and every integer $k$ with
$0 < |k| < j$,

$$F_{j(n+1)} = \frac{F_j}{F_k} \sum_{i=0}^{n}
\left(\frac{(-1)^{k+1} F_{j-k}}{F_k}\right)^{n-i} F_{ji+k}.$$

## Sources

- Gregory Dresden and Xiaoya Gao, "Further Extensions of Sury's Identity", Theorem 5, formula (53).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.fib_step_offset_sury_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/sury-s-identity-and-its-extensions/index.html#fib-step-offset-sury-sum).

## Offset step extension of Sury's identity, Lucas form

Let $F_n$ and $L_n$ be the
Fibonacci and Lucas numbers at integer indices. For all natural numbers $j$ and $n$ and every
integer $k$ with $|k| < j$,

$$F_{j(n+1)} = \frac{F_j}{L_k} \sum_{i=0}^{n}
\left(\frac{(-1)^k L_{j-k}}{L_k}\right)^{n-i} L_{ji+k}.$$

## Sources

- Gregory Dresden and Xiaoya Gao, "Further Extensions of Sury's Identity", Theorem 5, formula (54).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SuryIdentityExtensionsWanted.lucas_step_offset_sury_fib_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SuryIdentityExtensionsWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/sury-s-identity-and-its-extensions/index.html#lucas-step-offset-sury-fib-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sury's identity and its extensions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/sury-s-identity-and-its-extensions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/sury-s-identity-and-its-extensions)
