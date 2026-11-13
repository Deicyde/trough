---
declaration: section
origin: cited
lean: MetaMathlibExt.cohn_twice_square_lucas, MetaMathlibExt.cohn_square_lucas, MetaMathlibExt.cohn_square_fibonacci, MetaMathlibExt.cohn_twice_square_fibonacci
statement: formalized
proof: formalized
---

# Squares in Fibonacci and Lucas sequences

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-in-fibonacci-and-lucas-sequences/index.html).

## Cohn's theorem on Lucas numbers of the form $2x^2$

Let $L_n$ denote the Lucas numbers,
with $L_0 = 2$, $L_1 = 1$ and $L_{n+2} = L_{n+1} + L_n$. If $n$ and $x$ are natural numbers
with $n \ge 1$ and $L_n = 2x^2$, then $n = 6$.

This is the fourth claim of Theorem 2.1 of Keskin and Yosma.

Formalized by `MetaMathlibExt.cohn_twice_square_lucas`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/CohnTwiceSquareLucas.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/CohnTwiceSquareLucas.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-in-fibonacci-and-lucas-sequences/index.html#cohn-twice-square-lucas).

## Cohn's theorem on square Lucas numbers

Let $L_0 = 2$, $L_1 = 1$ and
$L_{n+2} = L_{n+1} + L_n$ be the Lucas numbers. If $n \ge 1$ and $L_n = x^2$ for some natural
number $x$, then $n = 1$ or $n = 3$.

This is the third claim of Theorem 2.1 of Keskin and Yosma, which they attribute to Cohn.

Formalized by `MetaMathlibExt.cohn_square_lucas`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/SquareFibonacciLucas.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/SquareFibonacciLucas.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-in-fibonacci-and-lucas-sequences/index.html#cohn-square-lucas).

## Cohn's theorem on square Fibonacci numbers

Let $F_n$ denote the Fibonacci numbers,
with $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$. If $n$ and $x$ are natural numbers
with $n \ge 1$ and $F_n = x^2$, then $n \in \{1, 2, 12\}$.

This is the first claim of Theorem 2.1 of Keskin and Yosma.

Formalized by `MetaMathlibExt.cohn_square_fibonacci`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/CohnSquareFibonacci.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/CohnSquareFibonacci.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-in-fibonacci-and-lucas-sequences/index.html#cohn-square-fibonacci).

## Cohn's theorem on Fibonacci numbers of the form $2x^2$

Let $F_n$ denote the Fibonacci
numbers, with $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$. If $n$ and $x$ are natural
numbers with $n \ge 1$ and $F_n = 2x^2$, then $n \in \{3, 6\}$.

This is the second claim of Theorem 2.1 of Keskin and Yosma.

Formalized by `MetaMathlibExt.cohn_twice_square_fibonacci`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/CohnTwiceSquareFibonacci.lean, line 507](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/CohnTwiceSquareFibonacci.lean#L507). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-in-fibonacci-and-lucas-sequences/index.html#cohn-twice-square-fibonacci).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Squares in Fibonacci and Lucas sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-in-fibonacci-and-lucas-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/squares-in-fibonacci-and-lucas-sequences)
