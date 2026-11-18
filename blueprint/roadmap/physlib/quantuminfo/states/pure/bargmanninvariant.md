---
declaration: module
origin: cited
lean: bargmannInvariantThree, bargmannPhaseThree, bargmannInvariantThree_degenerate, bargmannPhaseThree_degenerate, bargmannInvariantThree_reverse, bargmannPhaseThree_reverse, bargmannInvariantThree_cyclic, bargmannPhaseThree_cyclic
statement: formalized
proof: formalized
---

# Bargmann Invariant and Geometric Phase

The module `QuantumInfo.States.Pure.BargmannInvariant`, [QuantumInfo/States/Pure/BargmannInvariant.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BargmannInvariant.lean): 9 declarations, 9 with a docstring.

> The Bargmann invariant for three quantum states is the cyclic product
> of inner products `⟨ψ₁|ψ₂⟩ · ⟨ψ₂|ψ₃⟩ · ⟨ψ₃|ψ₁⟩`. Its argument is
> the geometric (Pancharatnam-Berry) phase accumulated around the
> geodesic triangle in projective Hilbert space.

## Important definitions

> * `bargmannInvariantThree`: the 3-vertex Bargmann invariant `Δ₃`
>  * `bargmannPhaseThree`: the geometric phase `arg(Δ₃)`

## Important results

> * `bargmannInvariantThree_degenerate`: identical states give `Δ₃ = 1`
>  * `bargmannPhaseThree_degenerate`: identical states give phase `= 0`
>  * `bargmannInvariantThree_reverse`: reversing conjugates `Δ₃`
>  * `bargmannPhaseThree_reverse`: reversing negates the phase (mod 2π)
>  * `bargmannInvariantThree_cyclic`: cyclic permutation preserves `Δ₃`
>  * `bargmannPhaseThree_cyclic`: cyclic permutation preserves the phase
>  * `norm_bargmannInvariantThree_le_one`: `‖Δ₃‖ ≤ 1` (via `Braket.norm_dot_le_one`)

## References

> * V. Bargmann, Note on Wigner's theorem on symmetry operations, J. Math. Phys. 5, 862–868 (1964).
>   [ref: bargmann1964]
> * S. Pancharatnam, Generalized theory of interference, and its applications, Proc. Indian Acad.
>   Sci. A 44, 247–262 (1956). [ref: pancharatnam1956]

**`bargmannInvariantThree`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BargmannInvariant.lean#L50).

> The three-vertex Bargmann invariant: `⟨ψ₁|ψ₂⟩ · ⟨ψ₂|ψ₃⟩ · ⟨ψ₃|ψ₁⟩`.
> This is a gauge-invariant complex number whose argument is the
> geometric phase of the geodesic triangle.

```lean
def bargmannInvariantThree (ψ₁ ψ₂ ψ₃ : Ket d) : ℂ
```

**`bargmannPhaseThree`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BargmannInvariant.lean#L54).

> The geometric (Pancharatnam-Berry) phase of three states.

```lean
def bargmannPhaseThree (ψ₁ ψ₂ ψ₃ : Ket d) : ℝ
```

## Degenerate triangles

**`bargmannInvariantThree_degenerate`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BargmannInvariant.lean#L62).

> The Bargmann invariant of three identical states is 1.

```lean
lemma bargmannInvariantThree_degenerate (ψ : Ket d) :
    bargmannInvariantThree ψ ψ ψ = 1
```

**`bargmannPhaseThree_degenerate`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BargmannInvariant.lean#L69).

> The geometric phase of three identical states is 0.

```lean
lemma bargmannPhaseThree_degenerate (ψ : Ket d) :
    bargmannPhaseThree ψ ψ ψ = 0
```

## Conjugacy

**`bargmannInvariantThree_reverse`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BargmannInvariant.lean#L77).

> Reversing the cyclic order conjugates the invariant.

```lean
lemma bargmannInvariantThree_reverse (ψ₁ ψ₂ ψ₃ : Ket d) :
    bargmannInvariantThree ψ₃ ψ₂ ψ₁ = starRingEnd ℂ (bargmannInvariantThree ψ₁ ψ₂ ψ₃)
```

**`bargmannPhaseThree_reverse`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BargmannInvariant.lean#L87).

> Reversing the cyclic order negates the geometric phase (mod 2π).

```lean
lemma bargmannPhaseThree_reverse (ψ₁ ψ₂ ψ₃ : Ket d) :
    (bargmannPhaseThree ψ₃ ψ₂ ψ₁ : Real.Angle) =
    -(bargmannPhaseThree ψ₁ ψ₂ ψ₃ : Real.Angle)
```

## Cyclic symmetry

**`bargmannInvariantThree_cyclic`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BargmannInvariant.lean#L97).

> Cyclic permutation of the three states preserves the Bargmann invariant.

```lean
lemma bargmannInvariantThree_cyclic (ψ₁ ψ₂ ψ₃ : Ket d) :
    bargmannInvariantThree ψ₂ ψ₃ ψ₁ = bargmannInvariantThree ψ₁ ψ₂ ψ₃
```

**`bargmannPhaseThree_cyclic`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BargmannInvariant.lean#L103).

> Cyclic permutation preserves the geometric phase.

```lean
lemma bargmannPhaseThree_cyclic (ψ₁ ψ₂ ψ₃ : Ket d) :
    bargmannPhaseThree ψ₂ ψ₃ ψ₁ = bargmannPhaseThree ψ₁ ψ₂ ψ₃
```

## Norm bounds

**`norm_bargmannInvariantThree_le_one`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BargmannInvariant.lean#L112).

> The Bargmann invariant has norm at most 1: each inner product factor
> is bounded by Cauchy-Schwarz on unit vectors.

```lean
lemma norm_bargmannInvariantThree_le_one (ψ₁ ψ₂ ψ₃ : Ket d) :
    ‖bargmannInvariantThree ψ₁ ψ₂ ψ₃‖ ≤ 1
```

## Depends on

- [QuantumInfo.States.Pure.Braket](braket.md)

## Sources

- [QuantumInfo/States/Pure/BargmannInvariant.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BargmannInvariant.lean)
