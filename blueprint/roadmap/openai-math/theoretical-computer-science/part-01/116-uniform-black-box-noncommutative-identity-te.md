---
declaration: section
origin: cited
lean: OAI.NCHitting.universal_hitting, OAI.RationalHitting.main
statement: formalized
proof: formalized
---

# 116. Uniform black-box noncommutative identity testing across characteristics

3 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For each characteristic, constructs in deterministic polynomial bit time a polynomial-dimensional matrix tuple detecting every nonzero division-free noncommutative formula of bounded size over any field of that characteristic. Rational formulas over ℚ also admit polynomial-size hitting lists whenever they have a defined rational-matrix evaluation.

## Uniform Matrix Hitting Points in Every Positive Characteristic

We construct a single matrix substitution that detects every nonzero size-*s* division-free noncommutative formula in *n* variables over every field of a given positive characteristic. One deterministic machine, given a promised prime *p* in binary and *n*, *s* in unary, outputs matrices over 𝔽$_{p}$ of dimension $O(n^3s^6)$ in polynomial bit time. The same tuple works with arbitrary extension-field coefficients, including in characteristic two. The construction also applies to the stated acyclic algebraic path programs.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/uniform-matrix-hitting-points-positive-characteristic.pdf).

## One Rational Matrix Hitting Point for Noncommutative Formulas

We construct, in deterministic polynomial bit time, one tuple of rational matrices that detects every nonzero polynomial computed by a noncommutative division-free formula of a prescribed size. The matrices have dimension $O(ns^2)$ for *n* variables and formula size *s*, and the same tuple works over every field of characteristic zero.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026.pdf); the Lean below formalizes results from it.

## Polynomial Hitting Lists for Noncommutative Rational Formulas

We construct, in deterministic polynomial bit time, a polynomial-size list of rational matrix tuples for noncommutative rational formulas over ℚ of bounded tree size. Every nonzero admissible formula has a defined, invertible value at one tuple, with no separate bounds on inverse nesting or rational constant heights. Matrix dimensions, entry bit lengths, and total output length are polynomially bounded.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization gives one explicit tuple of rational matrices that simultaneously detects every nonzero division-free noncommutative formula with at most $s$ gates in $n$ variables, for $n,s\ge1$. Evaluation at that tuple is a nonzero matrix over every characteristic-zero field.

The selected theorem states this universal hitting property. The paper's deterministic polynomial bit-construction bound and matrix-dimension bound $O(ns^2)$ are not separately asserted in it.

The formalized result constructs polynomial-size hitting lists for noncommutative rational formulas with rational constants, addition, multiplication, and inverse gates. Given the number of variables and a formula-size bound, one deterministic polynomial-time machine outputs rational matrix tuples of a common positive dimension. Every admissible nonzero formula within the size bound evaluates to an invertible matrix on some listed tuple. The matrix dimension, complete binary output length, and running time are all polynomially bounded.

## Lean: One rational matrix tuple hitting all bounded-size noncommutative formulas

```lean
theorem universal_hitting (n s : ℕ) (hn : 1 ≤ n) (hs : 1 ≤ s)
    (F : Type u_2) [Field F] [CharZero F] (f : Formula F n)
    (hsize : f.size ≤ s) (hf : ∃ w, f.coeff w ≠ 0) :
    f.eval (Matrix.scalar (Fin (dimension n s)))
      (fun i r q => (generator n s i r q : F)) ≠ 0
```

Stated in [FormulaHitting.lean, line 57](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FormulaHitting.lean#L57). Proved in [lean/OAI/Algebra/FormulaHitting/Hitting.lean, line 86](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Algebra/FormulaHitting/Hitting.lean#L86).

## Lean: Polynomial hitting lists for rational formulas

```lean
theorem main : MainStatement
```

Stated in [RationalHitting.lean, line 108](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/RationalHitting.lean#L108). Proved in [lean/OAI/Computability/RationalHitting/Main.lean, line 44](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/RationalHitting/Main.lean#L44). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/116.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/116.md)
