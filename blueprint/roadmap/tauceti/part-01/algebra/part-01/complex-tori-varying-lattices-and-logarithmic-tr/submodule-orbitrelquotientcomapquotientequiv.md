---
declaration: def
origin: cited
lean: Submodule.orbitRelQuotientComapQuotientEquiv
statement: formalized
---

# Submodule.orbitRelQuotientComapQuotientEquiv

For a linear map `f : M → M₂` and submodules `p ≤ M`, `q ≤ M₂`, consider the image `K` of
`f⁻¹(q)` and the image `K₀` of `ker f` in the orbit space of translation by `p`. The quotient
`K / K₀` is additively equivalent to `(q ∩ range f) / (q ∩ f(p))`, by the map sending the class
of the orbit of `x ∈ f⁻¹(q)` to the class of `f x`. Here the denominator `q ∩ f(p)` is the
pullback of `f(p)` to `q ∩ range f`; it is `f(p)` itself when `f(p) ⊆ q`.

For lattices `L ⊆ E`, `L' ⊆ E'` and a complex linear map `f` with `f(L) ⊆ L'`, `K = f⁻¹(L') / L`
is the kernel of the induced homomorphism of complex tori `E / L → E' / L'`, `K₀` is its identity
component, and this is the description of its component group as `(L' ∩ range f) / f(L)`.

```lean
Submodule.orbitRelQuotientComapQuotientEquiv.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2} [Ring R]
  [AddCommGroup M] [_root_.Module R M] (p : Submodule R M) {M₂ : Type u_3} [AddCommGroup M₂]
  [_root_.Module R M₂] (q : Submodule R M₂) (f : M →ₗ[R] M₂) :
  ↥(AddSubgroup.map p.orbitRelQuotientMkHom (Submodule.comap f q).toAddSubgroup) ⧸
      (AddSubgroup.map p.orbitRelQuotientMkHom f.ker.toAddSubgroup).addSubgroupOf
        (AddSubgroup.map p.orbitRelQuotientMkHom (Submodule.comap f q).toAddSubgroup) ≃+
    ↥(q ⊓ f.range) ⧸ Submodule.comap (q ⊓ f.range).subtype (Submodule.map f p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Submodule.orbitRelQuotientComapQuotientEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/Submodule/OrbitRelQuotient.html#Submodule.orbitRelQuotientComapQuotientEquiv).

## Sources

- [Tau Ceti documentation: `Submodule.orbitRelQuotientComapQuotientEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/Submodule/OrbitRelQuotient.html#Submodule.orbitRelQuotientComapQuotientEquiv)
- [Source of `Submodule.orbitRelQuotientComapQuotientEquiv` in TauCeti/Algebra/Module/Submodule/OrbitRelQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/Submodule/OrbitRelQuotient.lean#L332)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexTori/STATUS.md)
