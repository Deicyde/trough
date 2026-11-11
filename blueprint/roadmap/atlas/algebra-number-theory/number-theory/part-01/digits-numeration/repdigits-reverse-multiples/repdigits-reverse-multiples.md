---
declaration: section
origin: cited
lean: Nat.reverseDigits, MetaMathlibExt.finite_near_repdigit_perfect_powers, MetaMathlibExt.squares_aaabb_classification, MathlibExt.NumberTheory.Digits.TriangularRepdigitsWanted.triangular_numbers_single_repeated_digit
statement: formalized
---

# Repdigits, palindromes and reverse multiples: its own results

4 results, 1 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/index.html).

Repdigits, palindromes, reverse multiples and Young graphs, permutiples, digit reversal, special squares by digits.

## Digit reversal

For natural numbers $b$ and $n$ with $b \ge 2$, write
$n = \sum_{i\lt k} d_i b^i$ with digits $0 \le d_i < b$ and leading digit $d_{k-1} \ne 0$ (so $k = 0$
when $n = 0$). The base-$b$ reversal of $n$ is the natural number $\sum_{i\lt k} d_{k-1-i} b^i$. For
the bases $b = 0$ and $b = 1$ the reversal of $n$ is $n$ itself.

Trailing zeros of $n$ become leading zeros and are lost: in base $10$ the reversal of $120$ is
$21$.

Formalized by `Nat.reverseDigits`, a definition declared in [MathlibExt/Data/Nat/Digits/Reverse.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Data/Nat/Digits/Reverse.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/index.html#reverse-digits).

## Perfect powers with all decimal digits equal but one (Kihel–Luca)

Fix a natural number
$l \ge 3$. There are only finitely many perfect $l$-th powers $y = x^l$ ($x \in \mathbb{N}$) whose
decimal digits are all equal but one, that is, some digit $c$ occurs in the decimal
representation of $y$ and exactly one digit position of $y$ holds a digit other than $c$, apart
from the powers $10^{ln}$ ($n \in \mathbb{N}$) and, when $l = 3$, the cubes $8 \cdot 10^{3n}$
($n \in \mathbb{N}$).

## Sources

- Omar Kihel and Florian Luca, "Perfect Powers with All Equal Digits but One," Journal of Integer Sequences 8 (2005), Article 05.5.7, Theorem 1, lines 134–140, https://cs.uwaterloo.ca/journals/JIS/VOL8/Kihel/kihel7.tex.

Stated but not proved: `MetaMathlibExt.finite_near_repdigit_perfect_powers` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/NearRepdigitPerfectPowersWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/NearRepdigitPerfectPowersWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/index.html#finite-near-repdigit-perfect-powers).

## Squares with two blocks of repeated digits

Let $n$ be a perfect square whose decimal
representation, read from the most significant digit, consists of $r \ge 1$ copies of a digit
$a$ with $1 \le a \le 9$ followed by $s \ge 1$ copies of a digit $b$ with $0 \le b \le 9$. Then
$n$ is one of $16$, $25$, $36$, $49$, $64$, $81$, $144$, $225$, $441$, $1444$ and $7744$, or
there is a natural number $i$ such that $n = 10^{2i}$, $n = 4 \cdot 10^{2i}$ or
$n = 9 \cdot 10^{2i}$.

## Sources

- Omar Kihel and Florian Luca, "Perfect Powers With All Equal Digits But One," Journal of Integer Sequences 8 (2005), Article 05.5.7, Theorem, lines 273–279, https://cs.uwaterloo.ca/journals/JIS/VOL8/Kihel/kihel7.tex

Stated but not proved: `MetaMathlibExt.squares_aaabb_classification` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/SquaresAaabbClassificationWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/SquaresAaabbClassificationWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/index.html#squares-aaabb-classification).

## Triangular repdigits

The positive triangular numbers $n(n+1)/2$ with $n \ge 1$ whose
decimal representation consists of a single repeated digit are exactly $1$, $3$, $6$, $55$, $66$
and $666$.

## Sources

- Christian Hercher and Karl Fegert, "Triangular Numbers With a Single Repeated Digit", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.Digits.TriangularRepdigitsWanted.triangular_numbers_single_repeated_digit` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/TriangularRepdigitsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/TriangularRepdigitsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/index.html#triangular-numbers-single-repeated-digit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Repdigits, palindromes and reverse multiples](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples)
