---
declaration: module
origin: cited
lean: lorentzAlgebra.boostGenerator, lorentzAlgebra.rotationGenerator, lorentzAlgebra.boostGenerator_mem, lorentzAlgebra.rotationGenerator_mem, lorentzAlgebra.boostGenerator_transpose, lorentzAlgebra.boostGenerator_trace, lorentzAlgebra.rotationGenerator_transpose, lorentzAlgebra.rotationGenerator_trace
statement: formalized
proof: formalized
---

# Generators of the Lorentz algebra

The module `Physlib.Relativity.LorentzAlgebra.Basis`, [Physlib/Relativity/LorentzAlgebra/Basis.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basis.lean): 9 declarations, 9 with a docstring.

> Standard boost and rotation generators and the tangent of a finite boost curve.

## i. Overview

> This file defines the 6 standard generators of the Lorentz algebra so(1,3) :
> - **Boost generators** K₀, K₁, K₂: Generate Lorentz transformations (velocity changes)
> - **Rotation generators** J₀, J₁, J₂: Generate spatial rotations
>
> These generators form a basis for the 6-dimensional Lie algebra so(1,3), though the full
> basis structure (linear independence and spanning) is not yet proven here.
>
> - `boostGenerator i`: Infinitesimal boost in the i-th spatial direction. The native
>   boost curve parametrized by rapidity has tangent `-boostGenerator i` at zero.
> - `rotationGenerator i`: Infinitesimal rotation about the i-th axis following the
>   right-hand rule. Exponentiating this generator produces spatial rotations.
>
> Each generator satisfies the Lorentz algebra condition: Aᵀ η = -η A, where η is the
> Minkowski metric with signature (+,-,-,-).
>
> The boost generators are symmetric matrices with non-zero entries only in the time-space
> block, while rotation generators are antisymmetric matrices acting only on spatial indices.
>
> …

## ii. Key results

> - `boostGenerator_mem` and `rotationGenerator_mem`: the generators lie in the Lorentz algebra.
> - `hasDerivAt_boost_tanh_zero`: the rapidity boost curve has tangent the negative boost generator.

## iv. References

> * Weinberg, The Quantum Theory of Fields, Vol 1, Section 2.7. [ref: weinberg\_qft1]
> * Peskin & Schroeder, An Introduction to QFT, Appendix A. [ref: peskin\_schroeder\_qft]

## A. Generator definitions

**`lorentzAlgebra.boostGenerator`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basis.lean#L82).

> The boost generator K\_i in the Lorentz algebra so(1,3).
>
> This matrix generates infinitesimal Lorentz boosts in the i-th spatial direction.
> The matrix has non-zero entries only at positions (0, i+1) and (i+1, 0) with value 1,
> where we use the index convention 0 = time, 1,2,3 = space.
>
> ## Properties
> - Symmetric: K\_iᵀ = K\_i
> - Traceless: tr(K\_i) = 0
> - Satisfies Lorentz algebra condition: K\_iᵀ η = -η K\_i
>
> ## Physical Meaning
> The native boost curve `LorentzGroup.boost i (Real.tanh r)` has tangent `-K_i` at
> rapidity zero, as proved by `hasDerivAt_boost_tanh_zero`.

```lean
def boostGenerator (i : Fin 3) : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ
```

**`lorentzAlgebra.rotationGenerator`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basis.lean#L106).

> The rotation generator J\_i in the Lorentz algebra so(1,3).
>
> This matrix generates infinitesimal rotations about the i-th axis following the right-hand rule.
> The matrix acts only on spatial indices in the antisymmetric pattern characteristic of
> angular momentum generators.
>
> ## Properties
> - Antisymmetric: J\_iᵀ = -J\_i
> - Traceless: tr(J\_i) = 0
> - Satisfies Lorentz algebra condition: J\_iᵀ η = -η J\_i
>
> ## Structure
> - J\_0 (rotation about x-axis) : Acts on (y,z) components
> - J\_1 (rotation about y-axis) : Acts on (z,x) components
> - J\_2 (rotation about z-axis) : Acts on (x,y) components
>
> ## Physical Meaning
> Exponentiating θ·J\_i produces a finite rotation by angle θ about axis i.

```lean
def rotationGenerator (i : Fin 3) : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ
```

## B. Algebraic properties

**`lorentzAlgebra.boostGenerator_mem`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basis.lean#L122).

> The boost generator K\_i is in the Lorentz algebra.

```lean
lemma boostGenerator_mem (i : Fin 3) : boostGenerator i ∈ lorentzAlgebra
```

**`lorentzAlgebra.rotationGenerator_mem`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basis.lean#L129).

> The rotation generator J\_i is in the Lorentz algebra.

```lean
lemma rotationGenerator_mem (i : Fin 3) : rotationGenerator i ∈ lorentzAlgebra
```

**`lorentzAlgebra.boostGenerator_transpose`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basis.lean#L137).

> The boost generators are symmetric.

```lean
lemma boostGenerator_transpose (i : Fin 3) :
    (boostGenerator i)ᵀ = boostGenerator i
```

**`lorentzAlgebra.boostGenerator_trace`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basis.lean#L144).

> The boost generators are traceless.

```lean
lemma boostGenerator_trace (i : Fin 3) :
    Matrix.trace (boostGenerator i) = 0
```

**`lorentzAlgebra.rotationGenerator_transpose`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basis.lean#L150).

> The rotation generators are antisymmetric.

```lean
lemma rotationGenerator_transpose (i : Fin 3) :
    (rotationGenerator i)ᵀ = -rotationGenerator i
```

**`lorentzAlgebra.rotationGenerator_trace`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basis.lean#L157).

> The rotation generators are traceless.

```lean
lemma rotationGenerator_trace (i : Fin 3) :
    Matrix.trace (rotationGenerator i) = 0
```

## C. Rapidity derivatives

**`lorentzAlgebra.hasDerivAt_boost_tanh_zero`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basis.lean#L167).

> The tangent at zero of the finite boost curve parametrized by rapidity
> is the negative of the named boost generator.

```lean
lemma hasDerivAt_boost_tanh_zero (i : Fin 3) :
    HasDerivAt (fun r : ℝ => (LorentzGroup.boost i (Real.tanh r) (Real.abs_tanh_lt_one r)).1)
      (-boostGenerator i) 0
```

## Depends on

- [The Lorentz Algebra](basic.md)
- [Boosts in the Lorentz group](../lorentzgroup/boosts-basic.md)

## Sources

- [Physlib/Relativity/LorentzAlgebra/Basis.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basis.lean)
