---
declaration: section
origin: cited
lean: IntegerComplexity.Expr, IntegerComplexity.Expr.eval, IntegerComplexity.Expr.count, IntegerComplexity.exists_expr_of_pos, IntegerComplexity.Pred, IntegerComplexity.complexity, IntegerComplexity.complexity_le, IntegerComplexity.complexity_add_le
statement: formalized
---

# Integer complexity

59 results, 32 proved and 27 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html).

## Expressions built from one, addition and multiplication

An expression is either the
constant $1$, or a sum $e_1 + e_2$ of two expressions, or a product $e_1 \times e_2$ of two
expressions. Expressions are formal syntax trees, so the tree structure plays the role of
parentheses.

## Sources

- C2.

Formalized by `IntegerComplexity.Expr`, an inductive type declared in [MathlibExt/NumberTheory/IntegerComplexity.lean, line 20](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerComplexity.lean#L20). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#expr).

## Value of an expression

The value of an expression is the natural number obtained by
evaluating it: the constant $1$ has value $1$, the value of $e_1 + e_2$ is the sum of the values
of $e_1$ and $e_2$, and the value of $e_1 \times e_2$ is the product of their values.

## Sources

- C2.

Formalized by `IntegerComplexity.Expr.eval`, a definition declared in [MathlibExt/NumberTheory/IntegerComplexity.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerComplexity.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#eval).

## Number of ones in an expression

The number of ones of an expression is the number of
occurrences of the constant $1$ in it: the constant $1$ has one, and both $e_1 + e_2$ and
$e_1 \times e_2$ have as many as $e_1$ and $e_2$ together.

## Sources

- C3.

Formalized by `IntegerComplexity.Expr.count`, a definition declared in [MathlibExt/NumberTheory/IntegerComplexity.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerComplexity.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#count).

## Every positive integer is the value of an expression

For every natural number
$n > 0$ there is an expression whose value is $n$.

## Sources

- C2/C4 existence side.

Formalized by `IntegerComplexity.exists_expr_of_pos`, a theorem declared in [MathlibExt/NumberTheory/IntegerComplexity.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerComplexity.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#exists-expr-of-pos).

## Achievable numbers of ones

For a positive integer $n$ and a natural number $c$, the
predicate holds when some expression has value $n$ and exactly $c$ ones.

## Sources

- replaces Set S.

Formalized by `IntegerComplexity.Pred`, a definition declared in [MathlibExt/NumberTheory/IntegerComplexity.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerComplexity.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#pred).

## Integer complexity

The integer complexity of a positive integer $n$ is the least
number of ones in an expression whose value is $n$, that is, the least number of ones needed
to write $n$ using $1$, $+$, $\times$ and parentheses.

## Sources

- C4. Implemented via Nat.find on proved existential predicate.

Formalized by `IntegerComplexity.complexity`, a definition declared in [MathlibExt/NumberTheory/IntegerComplexity.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerComplexity.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity).

## Expressions bound the integer complexity from above

Let $n$ be a positive integer. If
an expression $e$ has value $n$, then the integer complexity of $n$ is at most the number of
ones of $e$.

## Sources

- C4.

Formalized by `IntegerComplexity.complexity_le`, a theorem declared in [MathlibExt/NumberTheory/IntegerComplexity.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerComplexity.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-le).

## Integer complexity of a sum

For all positive integers $a$ and $b$, the integer
complexity of $a + b$ is at most the sum of the integer complexities of $a$ and $b$.

Formalized by `IntegerComplexity.complexity_add_le`, a theorem declared in [MathlibExt/NumberTheory/IntegerComplexity.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerComplexity.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-add-le).

## Integer complexity of a product

For all positive integers $a$ and $b$, the integer
complexity of $ab$ is at most the sum of the integer complexities of $a$ and $b$.

Formalized by `IntegerComplexity.complexity_mul_le`, a theorem declared in [MathlibExt/NumberTheory/IntegerComplexity.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerComplexity.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-mul-le).

## Integer complexity extended to all natural numbers

For a natural number $n$, the value
$\lVert n \rVert$ is the integer complexity of $n$ when $n$ is positive, that is, the least number
of ones needed to write $n$ using $1$, $+$, $\times$ and parentheses, and $\lVert 0 \rVert = 0$.

Formalized by `MathlibExt.NumberTheory.IntegerComplexityWanted.cx`, a definition declared in [WantedExt/NumberTheory/IntegerComplexityWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IntegerComplexityWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#cx).

## Lower-bound function for integer complexity

For a natural number $n$, let $a$ be the
largest natural number with $3^a \le n$ when $n \ge 1$, and let $a = 0$ when $n = 0$. The function
$g$ on the natural numbers is given by $g(n) = 3a$ if $n < \frac{4}{3} \cdot 3^a$,
$g(n) = 3a + 1$ if $\frac{4}{3} \cdot 3^a \le n < 2 \cdot 3^a$, and $g(n) = 3a + 2$ if
$n \ge 2 \cdot 3^a$.

Formalized by `MathlibExt.NumberTheory.IntegerComplexityWanted.complexityLowerBoundG`, a definition declared in [WantedExt/NumberTheory/IntegerComplexityWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IntegerComplexityWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-lower-bound-g).

## Integer complexity as a minimum over factorizations and sums

Write
$\lVert m \rVert$ for the integer complexity of a positive integer $m$, the least number of ones
needed to write $m$ using $1$, $+$, $\times$ and parentheses. For every integer $n \ge 2$,
$\lVert n \rVert$ is the least element of the set consisting of the numbers
$\lVert d \rVert + \lVert n/d \rVert$ for the divisors $d \ge 2$ of $n$ and the numbers
$\lVert j \rVert + \lVert n - j \rVert$ for the integers $j$ with $1 \le j \le n/2$.

## Sources

- Juan Arias de Reyna, "Complexity of Natural Numbers", Proposition 1.

Stated but not proved: `MathlibExt.NumberTheory.IntegerComplexityWanted.complexity_eq_min` is written with `theorem_wanted` in [WantedExt/NumberTheory/IntegerComplexityWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IntegerComplexityWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-eq-min).

## A criterion for lower bounds on integer complexity

Write $\lVert n \rVert$ for the
integer complexity of a positive integer $n$, the least number of ones needed to write $n$ using
$1$, $+$, $\times$ and parentheses. Let $P$ be a real-valued function on the natural numbers with
$P(1) = 1$ such that $P(n + m) \le P(n) + P(m)$ and $P(nm) \le P(n) + P(m)$ for all positive
integers $n$ and $m$. Then $P(n) \le \lVert n \rVert$ for every positive integer $n$.

## Sources

- Juan Arias de Reyna, "Complexity of Natural Numbers", Proposition 2.

Stated but not proved: `MathlibExt.NumberTheory.IntegerComplexityWanted.le_complexity_of_subadditive` is written with `theorem_wanted` in [WantedExt/NumberTheory/IntegerComplexityWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IntegerComplexityWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#le-complexity-of-subadditive).

## Logarithmic lower bound for integer complexity

Write $\lVert n \rVert$ for the integer
complexity of a positive integer $n$, the least number of ones needed to write $n$ using $1$, $+$,
$\times$ and parentheses. For every positive integer $n$, $\log_2(1 + n) \le \lVert n \rVert$.

## Sources

- Juan Arias de Reyna, "Complexity of Natural Numbers", Corollary 1.

Stated but not proved: `MathlibExt.NumberTheory.IntegerComplexityWanted.logb_two_add_one_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/IntegerComplexityWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IntegerComplexityWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#logb-two-add-one-le).

## Integer complexity of $2^a 3^b$ for $a \le 2$

Write $\lVert n \rVert$ for the integer
complexity of a positive integer $n$, the least number of ones needed to write $n$ using $1$, $+$,
$\times$ and parentheses. For all natural numbers $a \le 2$ and $b$, not both zero,
$\lVert 2^a 3^b \rVert = 2a + 3b$.

## Sources

- Juan Arias de Reyna, "Complexity of Natural Numbers", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.IntegerComplexityWanted.complexity_two_pow_mul_three_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/IntegerComplexityWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IntegerComplexityWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-two-pow-mul-three-pow).

## Integers above $2^a 3^b$ have complexity above $2a + 3b$ when $a \le 2$ and $2a + 3b \ge 2$

Write $\lVert m \rVert$ for the integer complexity of a positive integer $m$, the least number
of ones needed to write $m$ using $1$, $+$, $\times$ and parentheses. Let $a \le 2$ and $b$ be
natural numbers with $2a + 3b \ge 2$. Then every natural number $m > 2^a 3^b$ satisfies
$\lVert m \rVert > 2a + 3b$.

## Sources

- Juan Arias de Reyna, "Complexity of Natural Numbers", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.IntegerComplexityWanted.complexity_lt_of_gt_extremal` is written with `theorem_wanted` in [WantedExt/NumberTheory/IntegerComplexityWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IntegerComplexityWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-lt-of-gt-extremal).

## The function $g$ bounds integer complexity from below

Write $\lVert n \rVert$ for the
integer complexity of a positive integer $n$, the least number of ones needed to write $n$ using
$1$, $+$, $\times$ and parentheses. For a positive integer $n$, let $a$ be the largest natural
number with $3^a \le n$, and let $g(n) = 3a$ if $n < \frac{4}{3} \cdot 3^a$, $g(n) = 3a + 1$ if
$\frac{4}{3} \cdot 3^a \le n < 2 \cdot 3^a$, and $g(n) = 3a + 2$ if $n \ge 2 \cdot 3^a$. Then
$g(n) \le \lVert n \rVert$ for every positive integer $n$.

## Sources

- Juan Arias de Reyna, "Complexity of Natural Numbers", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.IntegerComplexityWanted.complexityLowerBoundG_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/IntegerComplexityWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IntegerComplexityWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-lower-bound-g-le).

## Mahler–Popken expressions

For a natural number $m$, the $m$-ary Mahler–Popken expressions
are the formal expressions built from leaves using the binary operations $+$ and $\times$; the
tree structure plays the role of brackets. Each leaf carries a label $i \in \{0, \dots, m - 1\}$
(so there are $m$ kinds of leaf), and a leaf with label $i$ stands for the number
$i + 1 \in \{1, \dots, m\}$.

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.MahlerPopkenExpr`, an inductive type declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#mahler-popken-expr).

## Value of an $m$-ary expression

The natural number expressed by an $m$-ary Mahler–Popken
expression: the leaf with index $i \in \{0, \dots, m-1\}$ has value $i + 1$, and the value of a
sum or of a product of two expressions is the sum or the product of their values.

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.MahlerPopkenExpr.eval`, a definition declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#eval-2).

## Number of leaves of an $m$-ary expression

The number of leaf selections of an $m$-ary
Mahler–Popken expression, counting repetitions: a leaf counts $1$, and the count of a sum or of a
product of two expressions is the sum of their counts.

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.MahlerPopkenExpr.count`, a definition declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#count-2).

## Mahler–Popken complexity

For natural numbers $m$ and $n$, the $m$-ary Mahler–Popken
complexity $\lVert n \rVert_m$ is the smallest number of leaves (counted with repetition) of an
$m$-ary Mahler–Popken expression whose value is $n$: the smallest number of possibly repeated
selections from $\{1, \dots, m\}$ needed to express $n$ with addition, multiplication and legal
bracketing. If no expression has value $n$ (which happens exactly when $m = 0$ or $n = 0$), the
value is $0$.

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.mahlerPopkenComplexity`, a definition declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#mahler-popken-complexity).

## Every positive integer has an $m$-ary expression

For natural numbers $m \ge 1$ and
$n \ge 1$, there is an $m$-ary Mahler–Popken expression whose value is $n$ (for instance a sum of
ones).

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.exists_mahlerPopkenExpr_eval`, a theorem declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#exists-mahler-popken-expr-eval).

## The Mahler–Popken complexity is attained

For all natural numbers $m \ge 1$ and $n \ge 1$,
there is an $m$-ary Mahler–Popken expression whose value is $n$ and whose number of leaves
(counted with repetition) equals the $m$-ary Mahler–Popken complexity $\lVert n \rVert_m$.

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.mahlerPopkenComplexity_spec`, a theorem declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#mahler-popken-complexity-spec).

## Expressions bound the $m$-ary complexity from above

For natural numbers $m$ and $n$ and
every $m$-ary Mahler–Popken expression $e$ whose value is $n$, the $m$-ary Mahler–Popken
complexity $\|n\|_m$ is at most the number of leaves of $e$.

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.mahlerPopkenComplexity_min_le`, a theorem declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#mahler-popken-complexity-min-le).

## The $m$-ary complexity is positive

For natural numbers $m \ge 1$ and $n \ge 1$, the
$m$-ary Mahler–Popken complexity $\|n\|_m$ is positive.

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.mahlerPopkenComplexity_pos`, a theorem declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#mahler-popken-complexity-pos).

## Subadditivity of the $m$-ary complexity under addition

For natural numbers $m \ge 1$,
$a \ge 1$ and $b \ge 1$, the $m$-ary Mahler–Popken complexity $\|\cdot\|_m$ satisfies
$\|a + b\|_m \le \|a\|_m + \|b\|_m$.

This is the analogue of subadditivity under addition for the classical integer complexity.

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.mahlerPopkenComplexity_add_le`, a theorem declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#mahler-popken-complexity-add-le).

## Subadditivity of the $m$-ary complexity under multiplication

For natural numbers
$m \ge 1$, $a \ge 1$ and $b \ge 1$, the $m$-ary Mahler–Popken complexity $\|\cdot\|_m$ satisfies
$\|a b\|_m \le \|a\|_m + \|b\|_m$.

This is the analogue of subadditivity under multiplication for the classical integer
complexity.

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.mahlerPopkenComplexity_mul_le`, a theorem declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#mahler-popken-complexity-mul-le).

## Integer-complexity expressions as $1$-ary Mahler–Popken expressions

The translation of
an expression built from one, addition and multiplication into a $1$-ary Mahler–Popken expression
replaces each occurrence of $1$ by the leaf standing for $1$ and keeps every addition and
multiplication, so the expression tree is unchanged.

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.MahlerPopkenExpr.ofIntegerComplexityExpr`, a definition declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#of-integer-complexity-expr).

## $1$-ary Mahler–Popken expressions as integer-complexity expressions

The translation of a
$1$-ary Mahler–Popken expression into an expression built from one, addition and multiplication
replaces each leaf (the only leaf stands for $1$) by $1$ and keeps every addition and
multiplication, so the expression tree is unchanged.

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.MahlerPopkenExpr.toIntegerComplexityExpr`, a definition declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#to-integer-complexity-expr).

## The $1$-ary complexity is the integer complexity

For every natural number $n \ge 1$, the
$1$-ary Mahler–Popken complexity $\|n\|_1$ equals the classical integer complexity of $n$, the
least number of ones needed to write $n$ using $1$, $+$, $\times$ and parentheses.

This is the case $m = 1$ of Definition 1 in Campbell's paper (its Example 2).

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.mahlerPopkenComplexity_one_eq`, a theorem declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#mahler-popken-complexity-one-eq).

## Right-hand side of the Mahler–Popken recursion

For natural numbers $m$ and $n$, write
$\lVert k \rVert_m$ for the $m$-ary Mahler–Popken complexity of $k$. The recursion value of $n$
is the smallest of the sums $\lVert d \rVert_m + \lVert n/d \rVert_m$ over the divisors $d$ of
$n$ with $d \ne 1$ and $d \ne n$, and of the sums $\lVert \eta \rVert_m + \lVert n - \eta \rVert_m$
over $0 < \eta < n$; it is $0$ when there are no such sums. This is the right-hand side of the
recursion (9) in Campbell's paper.

Formalized by `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.mahlerPopkenRecursionValue`, a definition declared in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#mahler-popken-recursion-value).

## The $m$-ary complexity eventually satisfies its recursion

For every natural number
$m \ge 1$ there is $N$ such that for every $n \ge N$, the $m$-ary Mahler–Popken complexity
$\|n\|_m$ equals the right-hand side of the recursion (9), that is, the least of the values
$\|d\|_m + \|n/d\|_m$ over divisors $d$ of $n$ with $d \ne 1$ and $d \ne n$, and the values
$\|\eta\|_m + \|n - \eta\|_m$ over $0 < \eta < n$.

## Sources

- John M. Campbell, "A Binary Version of the Mahler-Popken Complexity Function", Proposition 1.

Stated but not proved: `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.mahlerPopkenComplexity_eq_recursionValue_eventually` is written with `theorem_wanted` in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#mahler-popken-complexity-eq-recursion-va).

## Recursion for the binary Mahler–Popken complexity

For every natural number $n \ge 3$,
the binary ($2$-ary) Mahler–Popken complexity $\lVert n \rVert_2$ equals the minimum of the sums
$\lVert d \rVert_2 + \lVert n/d \rVert_2$ over the divisors $d$ of $n$ with $d \ne 1$ and
$d \ne n$, and of the sums $\lVert \eta \rVert_2 + \lVert n - \eta \rVert_2$ over $0 < \eta < n$.
This is the recursion (9) for $m = 2$.

## Sources

- John M. Campbell, "A Binary Version of the Mahler-Popken Complexity Function", Proposition 1.

Stated but not proved: `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.mahlerPopkenComplexity_two_eq_recursionValue` is written with `theorem_wanted` in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#mahler-popken-complexity-two-eq-recursio).

## Logarithmic lower bound for the binary Mahler–Popken complexity

For every natural number
$n \ge 1$, the $2$-ary (binary) Mahler–Popken complexity $\|n\|_2$ satisfies $\log_2 n \le \|n\|_2$.

## Sources

- John M. Campbell, "A Binary Version of the Mahler-Popken Complexity Function", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.logb_two_le_mahlerPopkenComplexity_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#logb-two-le-mahler-popken-complexity-two).

## Upper bound for the binary Mahler–Popken complexity

For every natural number $n \ge 2$,
the binary ($2$-ary) Mahler–Popken complexity $\lVert n \rVert_2$ is at most
$\lfloor \log_2 n \rfloor + \nu_2(n) - 1$, where $\nu_2(n)$ is the number of ones in the base-$2$
expansion of $n$.

## Sources

- John M. Campbell, "A Binary Version of the Mahler-Popken Complexity Function", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.MahlerPopkenComplexityWanted.mahlerPopkenComplexity_two_le_log_add_digitCount_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MahlerPopkenComplexityWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#mahler-popken-complexity-two-le-log-add).

## Numbers built from copies of $l$

For natural numbers $l$, $k$ and $n$, the number $n$
can be built from $k$ copies of $l$ when $n$ is the value of an expression that uses exactly $k$
copies of $l$, combined by addition and multiplication with arbitrary parentheses. Inductively,
$l$ is built from $1$ copy, and if $x$ is built from $a$ copies and $y$ from $b$ copies, then
$x + y$ and $x y$ are built from $a + b$ copies.

Formalized by `MathlibExt.NumberTheory.TwoComplexityWanted.CanBuild`, an inductive type declared in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#can-build).

## The $l$-complexity of a natural number

For natural numbers $l$ and $n$, the
$l$-complexity $\|n\|_l$ of $n$ is the least number $k$ such that $n$ can be built from $k$
copies of $l$ using addition and multiplication (with arbitrary parentheses), and
$\|n\|_l = 0$ if $n$ cannot be built from copies of $l$ at all.

Formalized by `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL`, a definition declared in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l).

## Every build uses at least one copy

If $n$ can be obtained from $k$ copies of $l$ using
addition and multiplication, then $k \ge 1$.

Formalized by `MathlibExt.NumberTheory.TwoComplexityWanted.CanBuild.one_le`, a theorem declared in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#one-le).

## A buildable number is built from as many copies as its $l$-complexity

For natural
numbers $l$ and $n$, if $n$ can be built from some number of copies of $l$ using addition and
multiplication, then $n$ can be built in this way from $c$ copies of $l$, where $c$ is the
$l$-complexity of $n$.

Formalized by `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_spec`, a theorem declared in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-spec).

## The $l$-complexity is at most the size of any build

For natural numbers $l$, $k$ and
$n$, if $n$ can be built from $k$ copies of $l$ using addition and multiplication, then the
$l$-complexity of $n$ is at most $k$.

Formalized by `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_min_le`, a theorem declared in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-min-le).

## The $l$-complexity vanishes exactly on numbers that cannot be built

For natural
numbers $l$ and $n$, the $l$-complexity of $n$ is $0$ if and only if there is no $k$ such that
$n$ can be built from $k$ copies of $l$ using addition and multiplication.

Formalized by `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_eq_zero_iff`, a theorem declared in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-eq-zero-iff).

## Zhang's four exceptional forms

For natural numbers $m$ and $n$, $n$ has one of the four
exceptional forms for $m$ when one of the following holds:
(a) $n = 2^m + 2^{m_2} + 2^{m_3}$ for some natural numbers $m > m_2 > m_3 \ge 1$;
(b) $n = 2^m + 2^{m_2} + 2^{m_3} + 2^{m_4}$ for some natural numbers $m > m_2 > m_3 > m_4 \ge 2$
with $m + m_4 = m_2 + m_3$;
(c) $n = 2^m + 2^{m-3} + 2^{m_2} + 2^{m_2 - 1}$ for some natural number $m_2$ with
$m \ge m_2 + 3 \ge 6$;
(d) $m \ge 10$ and $n = 2^m + 2^{m-5} + 2^{m-6} + 2^{m-7}$.

These are the forms of Corollary 3 and Theorem 1(2) of Zhang's paper, which concern even $n$
with $2^m < n \le 2^{m+1}$ and 2-complexity $m + 2$.

Formalized by `MathlibExt.NumberTheory.TwoComplexityWanted.twoComplexityAddTwoForm`, a definition declared in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#two-complexity-add-two-form).

## The largest number built from $m$ copies of $l$

Let $l > 1$ and $m \ge 1$ be natural
numbers. Then $l^m$ can be built from exactly $m$ copies of $l$ using addition and
multiplication, and every natural number that can be built from $m$ copies of $l$ in this way
is at most $l^m$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.canBuild_max` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#can-build-max).

## Logarithmic bounds for the $l$-complexity

Write $\|n\|_l$ for the $l$-complexity of
$n$. Let $l > 1$ be a natural number and let $n$ be a positive multiple of $l$. Then
$\log_l n \le \|n\|_l \le l \log_l n - 1$, where $\log_l$ is the real logarithm to base $l$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Proposition 1.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.logb_le_complexityL_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#logb-le-complexity-l-le).

## The $l$-complexity of $l^m + l^{m'}$

Write $\|n\|_l$ for the $l$-complexity of $n$.
For natural numbers $l > 1$ and $m \ge m' \ge 1$, $\|l^m + l^{m'}\|_l = m + 1$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Corollary 1.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_pow_add_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-pow-add-pow).

## The 2-complexity of a power of two and of a sum of two powers of two

Write
$\|n\|_2$ for the $2$-complexity of $n$. For all natural numbers $m_1$ and $m_2$ with
$m_1 > m_2 \ge 1$, one has $\|2^{m_1}\|_2 = m_1$ and $\|2^{m_1} + 2^{m_2}\|_2 = m_1 + 1$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_two_pow_and_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-two-pow-and-add).

## An upper bound for the 2-complexity of a sum of distinct powers of two

Write
$\|n\|_2$ for the $2$-complexity of $n$. Let $S$ be a nonempty finite set of positive integers
with $k$ elements and largest element $m_1$. Then $\|\sum_{e \in S} 2^e\|_2 \le m_1 + k - 1$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_sum_two_pow_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-sum-two-pow-le).

## Logarithmic bounds for the 2-complexity (Zhang's Lemma 3(3))

Write $\|n\|_2$ for the
2-complexity of $n$: the least number of copies of $2$ from which $n$ can be built using addition
and multiplication, and $0$ if $n$ cannot be built. For every even natural number $n \ge 1$,
$\log_2 n \le \|n\|_2 \le 2 \log_2 n - 1$, where $\log_2$ is the real base-2 logarithm.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.logb_two_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#logb-two-bounds).

## A lower bound for the 2-complexity outside sums of two powers of two

Write
$\|n\|_2$ for the $2$-complexity of $n$. Let $n$ be a positive even integer that cannot be
written as $2^a + 2^b$ with natural numbers $a \le b$. Then $\log_2 n + 1 \le \|n\|_2$.

Since $n$ is even, the hypothesis says that $n$ is neither a power of $2$ nor a sum of two
distinct powers of $2$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.logb_two_add_one_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#logb-two-add-one-le-2).

## Adding a small multiple of $l$ to a multiple of $l^2$

Write $\|n\|_l$ for the
$l$-complexity of $n$. Let $l > 1$, let $b \ge 1$ be a multiple of $l^2$, let $a$ be a natural
number with $a \le l - 1$, and let $n = b + a l$. Then $\|n\|_l = \|b\|_l + a$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Proposition 2.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_decomp` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-decomp).

## Even $n$ with $2^m < n \le 2^{m+1}$ and 2-complexity $m + 1$

Write $\|n\|_2$ for the
2-complexity of $n$. Let $m \ge 1$ and let $n$ be an even natural number with
$2^m < n \le 2^{m+1}$. Then $\|n\|_2 = m + 1$ if and only if $n = 2^m + 2^t$ for some natural
number $t$ with $1 \le t \le m$.

The case $t = m$ gives $n = 2^{m+1}$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Proposition 3 and Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_eq_add_one_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-eq-add-one-iff).

## Four forms of even numbers with 2-complexity $m + 2$

Write $\|n\|_2$ for the
2-complexity of $n$. Let $m \ge 3$ and let $n$ be an even natural number with
$2^m < n \le 2^{m+1}$. Suppose that $n$ has one of the following forms, where all exponents
are natural numbers:
(a) $n = 2^m + 2^{m_2} + 2^{m_3}$ with $m > m_2 > m_3 \ge 1$;
(b) $n = 2^m + 2^{m_2} + 2^{m_3} + 2^{m_4}$ with $m > m_2 > m_3 > m_4 \ge 2$ and
$m + m_4 = m_2 + m_3$;
(c) $n = 2^m + 2^{m-3} + 2^{m_2} + 2^{m_2-1}$ with $m \ge m_2 + 3 \ge 6$;
(d) $n = 2^m + 2^{m-5} + 2^{m-6} + 2^{m-7}$ with $m \ge 10$.
Then $\|n\|_2 = m + 2$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Corollary 3.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_eq_add_two_of_form` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-eq-add-two-of-form).

## Even numbers in $(2^m, 2^{m+1})$ with 2-complexity $m + 2$

Write $\|n\|_2$ for the
2-complexity of $n$. Let $m \ge 3$ and let $n$ be an even natural number with
$2^m < n \le 2^{m+1}$. Then $\|n\|_2 = m + 2$ if and only if $n$ has one of the following
forms, where all exponents are natural numbers:
(a) $n = 2^m + 2^{m_2} + 2^{m_3}$ with $m > m_2 > m_3 \ge 1$;
(b) $n = 2^m + 2^{m_2} + 2^{m_3} + 2^{m_4}$ with $m > m_2 > m_3 > m_4 \ge 2$ and
$m + m_4 = m_2 + m_3$;
(c) $n = 2^m + 2^{m-3} + 2^{m_2} + 2^{m_2-1}$ with $m \ge m_2 + 3 \ge 6$;
(d) $n = 2^m + 2^{m-5} + 2^{m-6} + 2^{m-7}$ with $m \ge 10$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Proposition 4 and Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_eq_add_two_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-eq-add-two-iff).

## Lower bound $\log_2 n + 2$ for the 2-complexity (Zhang's Corollary 4)

Write $\|n\|_2$
for the 2-complexity of $n$: the least number of copies of $2$ from which $n$ can be built using
addition and multiplication, and $0$ if $n$ cannot be built. Let $m$ and $n$ be natural numbers
with $n$ even, $n \ge 1$ and $2^m < n \le 2^{m+1}$. Suppose that $n \ne 2^a + 2^b$ for all
natural numbers $a \le b$, and that $n$ has none of Zhang's four exceptional forms for $m$.
Then $\log_2 n + 2 \le \|n\|_2$, where $\log_2$ is the real base-2 logarithm.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Corollary 4.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.logb_two_add_two_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#logb-two-add-two-le).

## Lower bound for the 2-complexity of even sums of five or more distinct powers of two

Write $\|n\|_2$ for the 2-complexity of $n$. Let $n \ge 1$ be an even natural number and let $S$
be a finite set of natural numbers with at least five elements such that $n = \sum_{e \in S} 2^e$.
Then $\log_2 n + 2 \le \|n\|_2$, where $\log_2$ is the real base-2 logarithm.

This is a particular case of Corollary 4 of the source.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Corollary 4.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.logb_two_add_two_le_of_five_powers` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#logb-two-add-two-le-of-five-powers).

## The 2-complexity of $2^m \cdot 6^r$ for $1 \le r \le 7$

Write $\|n\|_2$ for the
$2$-complexity of $n$. For all natural numbers $m$ and $r$ with $1 \le r \le 7$, one has
$\|2^m \cdot 6^r\|_2 = m + 3r$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Proposition 5 and Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_two_pow_mul_six_pow_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-two-pow-mul-six-pow-eq).

## Bounds for the 2-complexity of $2^m \cdot 6^r$ when $8 \le r \le 9$

Write $\|n\|_2$ for
the $2$-complexity of $n$. For all natural numbers $m$ and $r$ with $8 \le r \le 9$, one has
$m + 3r - 1 \le \|2^m \cdot 6^r\|_2 \le m + 3r$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Proposition 5 and Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_two_pow_mul_six_pow_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-two-pow-mul-six-pow-bounds).

## The 2-complexity of $2^m \cdot 10^r$ for $1 \le r \le 4$

Write $\|n\|_2$ for the
$2$-complexity of $n$. For all natural numbers $m$ and $r$ with $1 \le r \le 4$, one has
$\|2^m \cdot 10^r\|_2 = m + 4r$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Proposition 6 and Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_two_pow_mul_ten_pow_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-two-pow-mul-ten-pow-eq).

## Bounds for the 2-complexity of $2^m \cdot 10^5$

Write $\|n\|_2$ for the $2$-complexity
of $n$. For every natural number $m$, one has $m + 19 \le \|2^m \cdot 10^5\|_2 \le m + 20$.

## Sources

- Pengcheng Zhang, "The 2-Complexity of Even Positive Integers", Proposition 6 and Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.TwoComplexityWanted.complexityL_two_pow_mul_ten_pow_five_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoComplexityWanted.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoComplexityWanted.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html#complexity-l-two-pow-mul-ten-pow-five-bo).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integer complexity](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/integer-complexity)
