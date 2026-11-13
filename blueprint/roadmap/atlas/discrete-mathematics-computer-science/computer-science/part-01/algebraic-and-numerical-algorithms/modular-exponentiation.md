---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation, Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_zero, Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_even, Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_odd, Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_ret_zero, Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_time_zero, Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_ret_even, Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_time_even
statement: formalized
proof: formalized
---

# Modular exponentiation

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html).

## Modular exponentiation

For natural numbers $a$, $b$ and $n$, modular exponentiation with
base $a$, exponent $b$ and modulus $n$ is the recursive procedure that returns $1$ if $b = 0$. If
$b > 0$ is even, it computes the result $d$ for exponent $b/2$ (same base and modulus) and returns
$d \cdot d \bmod n$. If $b$ is odd, it computes the result $d$ for exponent $b - 1$ and returns
$a \cdot d \bmod n$. Each even or odd step performs one multiplication, and the cost of the
procedure is the total number of multiplications performed.

## Sources

- CLRS4 §31.6, printed page 934, `MODULAR-EXPONENTIATION`, with one tick per multiplication.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation`, a definition declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation).

## Base case of modular exponentiation

For all natural numbers $a$ and $n$, modular
exponentiation with base $a$, exponent $0$ and modulus $n$ returns $1$ and performs no
multiplications.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-zero).

## Even step of modular exponentiation

Let $a$, $b$, $n$ be natural numbers with $b > 0$
and $b$ even. If modular exponentiation on base $a$, exponent $b/2$ and modulus $n$ returns the
value $d$ using $t$ multiplications, then on base $a$, exponent $b$ and modulus $n$ it returns
the value $(d \cdot d) \bmod n$ using $t + 1$ multiplications.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_even`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-even).

## Odd step of modular exponentiation

Let $a$, $b$, $n$ be natural numbers with $b$ odd.
If modular exponentiation on base $a$, exponent $b - 1$ and modulus $n$ returns the value $d$
using $t$ multiplications, then on base $a$, exponent $b$ and modulus $n$ it returns the value
$(a \cdot d) \bmod n$ using $t + 1$ multiplications.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_odd`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-odd).

## Modular exponentiation returns 1 at exponent zero

For all natural numbers $a$ and $n$,
modular exponentiation with base $a$, exponent $0$ and modulus $n$ returns $1$.

In particular the returned value is $1$ even when $n = 1$, so it is not reduced modulo $n$.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_ret_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-ret-zero).

## No multiplications at exponent zero

For all natural numbers $a$ and $n$, modular
exponentiation with base $a$, exponent $0$ and modulus $n$ performs no multiplications.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_time_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-time-zero).

## Value of the even step of modular exponentiation

Let $a$, $b$, $n$ be natural numbers
with $b > 0$ and $b$ even, and let $d$ be the value returned by modular exponentiation on base
$a$, exponent $b/2$ and modulus $n$. Then the value returned on base $a$, exponent $b$ and
modulus $n$ is $(d \cdot d) \bmod n$.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_ret_even`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-ret-even).

## Multiplication count in the even case

Let $a$, $b$ and $n$ be natural numbers with $b$
positive and even. Modular exponentiation with base $a$, exponent $b$ and modulus $n$ performs
exactly one more multiplication than it does with base $a$, exponent $b/2$ and modulus $n$.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_time_even`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-time-even).

## Value of the odd step of modular exponentiation

Let $a$, $b$, $n$ be natural numbers
with $b$ odd, and let $d$ be the value returned by modular exponentiation on base $a$, exponent
$b - 1$ and modulus $n$. Then the value returned on base $a$, exponent $b$ and modulus $n$ is
$(a \cdot d) \bmod n$.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_ret_odd`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-ret-odd).

## Multiplication count in the odd case

Let $a$, $b$ and $n$ be natural numbers with $b$ odd.
Modular exponentiation with base $a$, exponent $b$ and modulus $n$ performs exactly one more
multiplication than it does with base $a$, exponent $b - 1$ and modulus $n$.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_time_odd`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-time-odd).

## Modular exponentiation is correct up to reduction

For natural numbers $a$, $b$, $n$
with $n > 0$, including $b = 0$, the value $r$ returned by modular exponentiation on base $a$,
exponent $b$ and modulus $n$ satisfies $r \bmod n = a^b \bmod n$.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_ret_mod`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-ret-mod).

## Modular exponentiation with a reduced base

For natural numbers $a$, $b$, $n$ with
$n > 0$, the value $r$ returned by modular exponentiation on base $a$, exponent $b$ and
modulus $n$ satisfies $r \bmod n = (a \bmod n)^b \bmod n$.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_ret_mod_base`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-ret-mod-base).

## Modular exponentiation returns a reduced value

For natural numbers $a$, $b$, $n$ with
$b > 0$, the value $r$ returned by modular exponentiation on base $a$, exponent $b$ and
modulus $n$ satisfies $r \bmod n = r$ (with the convention $r \bmod 0 = r$).

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_ret_is_reduced`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-ret-is-reduced).

## Correctness of modular exponentiation

For natural numbers $a$, $b$, $n$ with $b > 0$
and $n > 0$, the value returned by modular exponentiation on base $a$, exponent $b$ and
modulus $n$ equals $a^b \bmod n$.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-correct).

## Modular exponentiation returns a value below the modulus

For natural numbers $a$, $b$,
$n$ with $b > 0$ and $n > 0$, the value returned by modular exponentiation on base $a$,
exponent $b$ and modulus $n$ is less than $n$.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-lt).

## Modular exponentiation returns the least residue

For natural numbers $a$, $b$, $n$ with
$b > 0$ and $n > 0$, the value $r$ returned by modular exponentiation on base $a$, exponent $b$
and modulus $n$ satisfies $r = a^b \bmod n$ and $r < n$.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_is_leastResidue`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-is-least-residue).

## Least residue at exponent zero

For all natural numbers $a$ and $n$ with $n > 1$, the value
returned by modular exponentiation with base $a$, exponent $0$ and modulus $n$ equals $a^0 \bmod n$
and is less than $n$.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_zero_is_leastResidue`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-zero-is-least-res).

## Unreduced result at modulus one

For every natural number $a$, modular exponentiation with
base $a$, exponent $0$ and modulus $1$ returns $1$, whereas $a^0 \bmod 1 = 0$.

The base case of the CLRS procedure returns $1$ without reducing it modulo the modulus; this
boundary case keeps that visible.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_zero_modulus_one`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-zero-modulus-one).

## The multiplication count depends only on the exponent

For all natural numbers $a$, $a'$,
$b$, $n$ and $n'$, modular exponentiation performs the same number of multiplications with base
$a$, exponent $b$ and modulus $n$ as with base $a'$, exponent $b$ and modulus $n'$.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_time_independent`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-time-independent).

## Multiplication count of modular exponentiation

Let $a$, $b$ and $n$ be natural numbers
with $b > 0$, and let $\beta = \lfloor \log_2 b \rfloor + 1$ be the number of binary digits of $b$.
The number of multiplications performed by modular exponentiation with base $a$, exponent $b$ and
modulus $n$ is at least $\beta$ and at most $2\beta - 1$.

Formalized by `Cslib.Algorithms.Lean.ModularExponentiation.modularExponentiation_time_bounds`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularExponentiation.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html#modular-exponentiation-time-bounds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Modular exponentiation](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/algebraic-and-numerical-algorithms/modular-exponentiation)
