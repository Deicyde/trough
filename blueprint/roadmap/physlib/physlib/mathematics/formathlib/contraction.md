---
declaration: module
origin: cited
lean: Module.Basis.coordPairing, Module.Basis.coordPairing_tmul_basis, Module.Basis.coordPairing_tmul, Module.Basis.coordPairing_basis_basis, Module.Basis.eq_coordPairing, Module.Basis.coordPairing_comm, Module.Basis.isPerfPair_coordPairing, Module.Basis.coordPairing_invariant
statement: formalized
proof: formalized
---

# The coordinate pairing of two bases

The module `Physlib.Mathematics.ForMathlib.Contraction`, [Physlib/Mathematics/ForMathlib/Contraction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Contraction.lean): 8 declarations, 8 with a docstring.

> Two bases with the same labels pair two modules by their coordinates.

## i. Overview

> Mathlib pairs a module `M` with its own dual. In physics the space paired with `M` is often a
> type of its own with its own basis, not `Module.Dual M`. Covectors `w_μ`, with the basis `e^μ`,
> pair with vectors `x^μ`, with the basis `e_μ`, as `x^μ w_μ = ∑ μ, x^μ w_μ`. This file gives that
> pairing for any two modules `M` and `N` with bases `b` and `b'` labelled by the same finite type
> `ι`, and shows that it identifies `N` with the dual of `M`, so Mathlib's results on duals apply.
>
> The coordinate pairing `coordPairing` sends `x ⊗ y` to `∑_I (b x)_I (b' y)_I`. It is Mathlib's
> `b'.toDual`, applied after the equivalence `b.equiv b'` that sends `b I` to `b' I`. The two bases
> are dual for it, it is the only pairing for which they are, and it is a perfect pairing in
> Mathlib's sense. When the two modules carry representations and some invariant pairing makes the
> bases dual, the coordinate pairing is that pairing, so it is invariant.

## ii. Key results

> - `Module.Basis.coordPairing` : the coordinate pairing `∑_I (b x)_I (b' y)_I` of two bases with
>   the same labels.
> - `Module.Basis.coordPairing_basis_basis` : the two bases are dual for the coordinate pairing, and
>   `Module.Basis.eq_coordPairing` : it is the only such pairing.
> - `Module.Basis.isPerfPair_coordPairing` : the coordinate pairing is a perfect pairing.
> - `Module.Basis.coordPairing_invariant` : the coordinate pairing is invariant when an invariant
>   pairing makes the bases dual.

## iv. References

> There are no known references for the material in this module.

## A. The coordinate pairing of two bases

**`Module.Basis.coordPairing`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Contraction.lean#L69).

> The coordinate pairing `M ⊗ N → R` of two bases with the same labels. It sends `x ⊗ y` to
> `b'.toDual x' y`, where `x'` is the vector of `N` with the coordinates of `x`.

```lean
noncomputable def coordPairing (b : Module.Basis ι R M) (b' : Module.Basis ι R N) :
    M ⊗[R] N →ₗ[R] R
```

**`Module.Basis.coordPairing_tmul_basis`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Contraction.lean#L74).

> Pairing with the second basis reads off a coordinate, `b.coordPairing b' (x ⊗ₜ b' J) = x_J`.

```lean
lemma coordPairing_tmul_basis (b : Module.Basis ι R M) (b' : Module.Basis ι R N) (x : M) (J : ι) :
    b.coordPairing b' (x ⊗ₜ[R] b' J) = b.equivFun x J
```

**`Module.Basis.coordPairing_tmul`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Contraction.lean#L79).

> `b.coordPairing b' (x ⊗ₜ y) = ∑_I (b x)_I (b' y)_I`.

```lean
lemma coordPairing_tmul (b : Module.Basis ι R M) (b' : Module.Basis ι R N) (x : M) (y : N) :
    b.coordPairing b' (x ⊗ₜ[R] y) = ∑ I, b.equivFun x I * b'.equivFun y I
```

**`Module.Basis.coordPairing_basis_basis`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Contraction.lean#L85).

> The two bases are dual, `b.coordPairing b' (b I ⊗ₜ b' J) = δ_{IJ}`.

```lean
lemma coordPairing_basis_basis (b : Module.Basis ι R M) (b' : Module.Basis ι R N) (I J : ι) :
    b.coordPairing b' (b I ⊗ₜ[R] b' J) = if I = J then 1 else 0
```

**`Module.Basis.eq_coordPairing`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Contraction.lean#L90).

> A pairing for which the two bases are dual is the coordinate pairing.

```lean
lemma eq_coordPairing (b : Module.Basis ι R M) (b' : Module.Basis ι R N) (p : M ⊗[R] N →ₗ[R] R)
    (h : ∀ I J, p (b I ⊗ₜ[R] b' J) = if I = J then 1 else 0) : p = b.coordPairing b'
```

**`Module.Basis.coordPairing_comm`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Contraction.lean#L97).

> Swapping the factors swaps the bases,
> `b.coordPairing b' (x ⊗ₜ y) = b'.coordPairing b (y ⊗ₜ x)`.

```lean
lemma coordPairing_comm (b : Module.Basis ι R M) (b' : Module.Basis ι R N) (x : M) (y : N) :
    b.coordPairing b' (x ⊗ₜ[R] y) = b'.coordPairing b (y ⊗ₜ[R] x)
```

**`Module.Basis.isPerfPair_coordPairing`**, an instance, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Contraction.lean#L102).

> The coordinate pairing of two bases with the same labels is a perfect pairing.

```lean
instance isPerfPair_coordPairing (b : Module.Basis ι R M) (b' : Module.Basis ι R N) :
    (TensorProduct.curry (b.coordPairing b')).IsPerfPair
```

## B. Invariance of the coordinate pairing

**`Module.Basis.coordPairing_invariant`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Contraction.lean#L124).

> The coordinate pairing is invariant when an invariant pairing `p` makes the bases dual, since
> then `p` is the coordinate pairing.

```lean
lemma coordPairing_invariant {G : Type*} [Monoid G] {ρ : Representation R G M}
    {ρ' : Representation R G N} {b : Module.Basis ι R M} {b' : Module.Basis ι R N}
    (p : (ρ.tprod ρ').IntertwiningMap (Representation.trivial R G R))
    (h : ∀ I J, p (b I ⊗ₜ b' J) = if I = J then 1 else 0) (g : G) (x : M) (y : N) :
    b.coordPairing b' (ρ g x ⊗ₜ ρ' g y) = b.coordPairing b' (x ⊗ₜ y)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/Contraction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Contraction.lean)
