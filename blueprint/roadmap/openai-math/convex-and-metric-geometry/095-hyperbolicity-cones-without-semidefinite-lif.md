---
declaration: section
origin: cited
lean: OAI.Paper256.main_result
statement: formalized
proof: formalized
---

# 095. Hyperbolicity cones without semidefinite lifts

3 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Disproves the Projected Lax conjecture: some hyperbolicity cones are not spectrahedral shadows. The examples admit no exact finite affine semidefinite lift, regardless of the number of auxiliary variables or the real coefficients used. This also disproves the generalized Lax conjecture that every hyperbolicity cone is spectrahedral.

## Hyperbolicity Cones Without Semidefinite Lifts

We prove that not every hyperbolicity cone is a spectrahedral shadow: some closed hyperbolicity cones admit no finite affine semidefinite lift, even with arbitrary real coefficients and any finite number of auxiliary variables. This disproves the Projected Lax Conjecture and hence the generalized Lax conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026/nonliftable-hyperbolicity.pdf).

## A nonspectrahedral hyperbolicity cone

We construct a homogeneous polynomial of degree 16 in 23 real variables whose hyperbolicity cone has no representation by a finite homogeneous real symmetric linear matrix inequality. This disproves the geometric Generalized Lax conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026/nonspectrahedral-hyperbolicity-cone.pdf); the Lean below formalizes results from it.

## An Exact Semidefinite Lift of a Nonspectrahedral Hyperbolicity Cone

We construct an exact semidefinite lift of the explicit nonspectrahedral hyperbolicity cone in twenty-three variables defined in the companion paper. The lift is a homogeneous real symmetric pencil of size 100 with 307 auxiliary variables and represents the entire closed cone, including every point with singular *X*. Thus, although this cone has no semidefinite representation in its original coordinates, it admits one when auxiliary variables are allowed. The stated sizes are not claimed to be minimal.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026/Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone.pdf).

## The Lean formalization

The generalized Lax conjecture predicts that every hyperbolicity cone is spectrahedral. The formalized counterexample is an explicit homogeneous polynomial of degree $20$ in $23$ real variables. It is hyperbolic, but its closed hyperbolicity cone cannot be represented as the positive-semidefinite region of any finite real symmetric linear matrix pencil, in any positive matrix size.

## Lean: Nonspectrahedral hyperbolicity cone

```lean
theorem main_result :
    Module.finrank ℝ Ambient = 23 ∧
    polynomial.IsHomogeneous 20 ∧
    polynomial.totalDegree = 20 ∧
    MvPolynomial.eval (coordinates basePoint) polynomial = 1 ∧
    (∀ (x : Ambient) (z : ℂ), (linePolynomial x).aeval z = 0 → z.im = 0) ∧
    ∀ (N : ℕ) (_hN : 0 < N) (L : Ambient →ₗ[ℝ] Sym N),
      cone ≠ {x | (L x : Mat N ℝ).PosSemidef}
```

Stated in [HyperbolicCones.lean, line 67](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HyperbolicCones.lean#L67). Proved in [lean/OAI/Analysis/HyperbolicCones/Main.lean, line 25](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/HyperbolicCones/Main.lean#L25). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/095.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/095.md)
