---
declaration: module
origin: cited
lean: Invariant.jarlskogℂCKM, Invariant.jarlskogℂCKM_equiv, Invariant.jarlskogℂ, Invariant.VusVubVcdSq, Invariant.mulExpδ₁₃
statement: formalized
proof: formalized
---

# Invariants of the CKM Matrix

The module `Physlib.Particles.FlavorPhysics.CKMMatrix.Invariants`, [Physlib/Particles/FlavorPhysics/CKMMatrix/Invariants.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Invariants.lean): 5 declarations, 5 with a docstring.

> The CKM matrix is only defined up to an equivalence.
>
> This file defines some invariants of the CKM matrix, which are well-defined with respect to
> this equivalence.
>
> Of note, this file defines the complex jarlskog invariant.

**`Invariant.jarlskogℂCKM`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Invariants.lean#L30).

> The complex jarlskog invariant for a CKM matrix.

```lean
def jarlskogℂCKM (V : CKMMatrix) : ℂ
```

**`Invariant.jarlskogℂCKM_equiv`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Invariants.lean#L34).

> The complex jarlskog invariant is equal for equivalent CKM matrices.

```lean
lemma jarlskogℂCKM_equiv (V U : CKMMatrix) (h : V ≈ U) :
    jarlskogℂCKM V = jarlskogℂCKM U
```

**`Invariant.jarlskogℂ`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Invariants.lean#L45).

> The complex jarlskog invariant for an equivalence class of CKM matrices.

```lean
def jarlskogℂ : Quotient CKMMatrixSetoid → ℂ
```

**`Invariant.VusVubVcdSq`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Invariants.lean#L51).

> An invariant for CKM matrices corresponding to the square of the absolute values
> of the `us`, `ub` and `cb` elements multiplied together divided by `(VudAbs V ^ 2 + VusAbs V ^2)`.

```lean
def VusVubVcdSq (V : Quotient CKMMatrixSetoid) : ℝ
```

**`Invariant.mulExpδ₁₃`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Invariants.lean#L56).

> An invariant for CKM matrices. The argument of this invariant is `δ₁₃` in the
> standard parameterization.

```lean
def mulExpδ₁₃ (V : Quotient CKMMatrixSetoid) : ℂ
```

## Depends on

- [The CKM Matrix](ckmmatrix-basic.md)

## Sources

- [Physlib/Particles/FlavorPhysics/CKMMatrix/Invariants.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Invariants.lean)
