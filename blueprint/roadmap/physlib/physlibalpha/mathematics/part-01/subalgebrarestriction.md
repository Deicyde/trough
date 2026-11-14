---
declaration: module
origin: cited
lean: Subalgebra.polyRange, Subalgebra.monomial_mem_polyRange, Subalgebra.mem_range_mapAlgHom_of_adjoin, Subalgebra.mapAlgHom_val_injective, Subalgebra.polyRestrict, Subalgebra.mapAlgHom_polyRestrict, Subalgebra.polyRestrict_eq_monomial_iff
statement: formalized
proof: formalized
---

# Restricting a polynomial-valued algebra map to a subalgebra

The module `PhyslibAlpha.Mathematics.SubalgebraRestriction`, [PhyslibAlpha/Mathematics/SubalgebraRestriction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SubalgebraRestriction.lean): 7 declarations, 6 with a docstring.

## i. Overview

> A grading of an algebra `A` is often recorded by an algebra map `f : A →ₐ[R] A[X]`, the
> weight-`n` part being the eigenspace on which `f` is the monomial `X ^ n`. A subalgebra `S`
> of `A` inherits such a grading exactly when `f` carries `S` into the polynomials with
> coefficients in `S`, and this file supplies the two steps that gives.
>
> Section A reduces the closure condition to the generators: since `f` is an algebra map and
> the polynomials with coefficients in `S` form a subalgebra of `A[X]`, it is enough that
> each generator lands there. Section B turns the closure condition into an algebra map
> `S →ₐ[R] S[X]`, through the injection of `S[X]` into `A[X]`, and records that an eigenvalue
> equation in `S` is the ambient one.
>
> Nothing here is about any particular algebra. It is stated for an arbitrary `S` so that it
> can be used at concrete algebras, where unfolding instances to check the corresponding
> statement directly would be expensive.

## ii. Key results

> - `Subalgebra.mem_range_mapAlgHom_of_adjoin` : the closure condition follows from the
>   generators.
> - `Subalgebra.polyRestrict` : the restricted map `S →ₐ[R] S[X]`.
> - `Subalgebra.polyRestrict_eq_monomial_iff` : an eigenvalue equation in `S` is the ambient
>   one.

## iv. References

> * None.

## A. Closure from the generators

**`Subalgebra.polyRange`**, an abbrev, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SubalgebraRestriction.lean#L61).

> The polynomials with coefficients in a subalgebra, as a subalgebra of the polynomials
> with coefficients in the ambient algebra.

```lean
noncomputable abbrev polyRange (S : Subalgebra R A) : Subalgebra R (Polynomial A)
```

**`Subalgebra.monomial_mem_polyRange`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SubalgebraRestriction.lean#L65).

> A monomial with a coefficient in `S` has coefficients in `S`.

```lean
lemma monomial_mem_polyRange {S : Subalgebra R A} {n : ℕ} {y : A} (hy : y ∈ S) :
    Polynomial.monomial n y ∈ S.polyRange
```

**`Subalgebra.mem_range_mapAlgHom_of_adjoin`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SubalgebraRestriction.lean#L72).

> If an algebra map into the polynomials sends every generator of an adjoined subalgebra
> into the polynomials over `S`, it sends the whole subalgebra there: the condition cuts out
> a subalgebra, and the generators lie in it.

```lean
lemma mem_range_mapAlgHom_of_adjoin {G : Set A} {f : A →ₐ[R] Polynomial A}
    (S : Subalgebra R A) (hgen : ∀ y ∈ G, f y ∈ S.polyRange)
    {x : A} (hx : x ∈ Algebra.adjoin R G) : f x ∈ S.polyRange
```

## B. The restricted map

**`Subalgebra.mapAlgHom_val_injective`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SubalgebraRestriction.lean#L88).

> Polynomials over a subalgebra inject into polynomials over the ambient algebra.

```lean
lemma mapAlgHom_val_injective (S : Subalgebra R A) :
    Function.Injective (Polynomial.mapAlgHom S.val)
```

**`Subalgebra.polyRestrict`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SubalgebraRestriction.lean#L95).

> An algebra map into the polynomials, restricted to a subalgebra it carries into the
> polynomials over that subalgebra.

```lean
noncomputable def polyRestrict (S : Subalgebra R A) (f : A →ₐ[R] Polynomial A)
    (hf : ∀ x : S, f (x : A) ∈ S.polyRange) : S →ₐ[R] Polynomial S
```

**`Subalgebra.mapAlgHom_polyRestrict`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SubalgebraRestriction.lean#L101).

```lean
lemma mapAlgHom_polyRestrict {S : Subalgebra R A} {f : A →ₐ[R] Polynomial A}
    (hf : ∀ x : S, f (x : A) ∈ S.polyRange) (x : S) :
    Polynomial.mapAlgHom S.val (S.polyRestrict f hf x) = f (x : A)
```

**`Subalgebra.polyRestrict_eq_monomial_iff`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SubalgebraRestriction.lean#L108).

> An eigenvalue equation for the restricted map is the ambient eigenvalue equation.

```lean
lemma polyRestrict_eq_monomial_iff {S : Subalgebra R A} {f : A →ₐ[R] Polynomial A}
    (hf : ∀ x : S, f (x : A) ∈ S.polyRange) {n : ℕ} (x : S) :
    S.polyRestrict f hf x = Polynomial.monomial n x
      ↔ f (x : A) = Polynomial.monomial n (x : A)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/SubalgebraRestriction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SubalgebraRestriction.lean)
