---
declaration: module
origin: cited
lean: ConjModule.instAlgebra, conjDualEquiv, Representation.conj, Representation.conj_apply, Representation.conj_trivial_apply, Representation.conj_trivial_dual_apply, ConjModule.map, ConjModule.map_apply
statement: formalized
proof: formalized
---

# Algebras, duals and representations on a conjugate module

The module `PhyslibAlpha.Mathematics.Modules.ConjModule`, [PhyslibAlpha/Mathematics/Modules/ConjModule.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean): 29 declarations (1 instance with no name), 14 with a docstring.

> The conjugate module of an algebra, the conjugate dual, and the conjugate of a representation.

## i. Overview

> `Physlib.Mathematics.Modules.ConjModule` carries `ConjModule M`, the module `M` with scalars
> acting through `star`, together with the conjugate-linear equivalence `conjEquiv`. This module
> extends that in three directions, all of which a conjugate Weyl field needs.
>
> First, when the module is a ring the conjugate module is a ring too, and the conjugate module
> of a `k`-algebra is a `k`-algebra: the same multiplication, with scalars acting through `star`.
>
> Second, the dual of `M` and the dual of `ConjModule M` are conjugate-linearly equivalent, by
> `conjDualEquiv`, so a linear functional on a field has a conjugate functional on the conjugate
> field.
>
> Third, a representation `ρ` of `G` on `M` has a conjugate representation `ρ.conj` of `G` on
> `ConjModule M`, given by the same maps `ρ g` read through `conjEquiv`. Conjugation commutes
> with the constructions representations are built from: it is involutive, it passes through
> products and `Pi` types, and over `ℂ` it turns a complex-linear endomorphism into its
> conjugate.

## ii. Key results

> - `ConjModule.instAlgebra` : the conjugate module of a `k`-algebra is a `k`-algebra.
> - `ConjModule.conjDualEquiv` : the dual of `M` and the dual of `ConjModule M` are
>   conjugate-linearly equivalent.
> - `Representation.conj` : the conjugate of a representation.
> - `ConjModule.prodEquiv`, `ConjModule.piEquiv` : conjugation commutes with products.

## iv. References

> The conjugate module itself is in `Physlib.Mathematics.Modules.ConjModule`.

## A. The conjugate module of an algebra

**An instance with no name**, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L75).

```lean
instance : Ring (ConjModule A)
```

**`ConjModule.instAlgebra`**, an instance, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L82).

> The conjugate module of a `k`-algebra is a `k`-algebra: the same ring, with scalars
> acting through `star`.

```lean
instance instAlgebra [Algebra k A] : Algebra k (ConjModule A)
```

## B. The conjugate dual

**`conjDualEquiv`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L96).

> The canonical conjugate-linear equivalence between the dual of a module `M` and
> the dual of its conjugate.

```lean
def conjDualEquiv : Module.Dual k M ≃ₛₗ[starRingEnd k] Module.Dual k (ConjModule M)
```

## C. The conjugate of a representation

**`Representation.conj`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L127).

> The conjugate of a representation `ρ` of `G` on `M`: the same maps `ρ g`, acting on
> `ConjModule M` through `conjEquiv`.

```lean
def _root_.Representation.conj {G} [Group G] (ρ : Representation k G M) :
    Representation k G (ConjModule M)
```

**`Representation.conj_apply`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L138).

```lean
lemma _root_.Representation.conj_apply {G} [Group G] (ρ : Representation k G M) (g : G)
    (m : ConjModule M) :
    ρ.conj g m = conjEquiv (k := k) (M := M) (ρ g ((conjEquiv (k := k) (M := M)).symm m))
```

**`Representation.conj_trivial_apply`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L143).

> The conjugate of the trivial representation acts trivially.

```lean
lemma _root_.Representation.conj_trivial_apply {G : Type*} [Group G] (g : G)
    (m : ConjModule M) : (Representation.trivial k G M).conj g m = m
```

**`Representation.conj_trivial_dual_apply`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L149).

> The dual of the conjugate of the trivial representation acts trivially.

```lean
lemma _root_.Representation.conj_trivial_dual_apply {G : Type*} [Group G] (g : G)
    (φ : Module.Dual k (ConjModule M)) :
    ((Representation.trivial k G M).conj).dual g φ = φ
```

## D. Functoriality, and conjugation of tensor products

> Conjugation is monoidal: `ConjModule M ⊗ ConjModule N ≃ ConjModule (M ⊗ N)`, the identity
> on pure tensors. The map is honestly `k`-linear because the twist on each factor cancels
> against the twist on the target.
>
> Everything below routes through `conjEquiv` rather than relying on definitional unfolding
> of the `ConjModule` synonym. Writing `m ⊗ₜ n` for `m : ConjModule M` makes elaboration
> pick the *twisted* module instances, landing in the wrong tensor product; converting
> explicitly with `conjEquiv` fixes every instance by construction.

**`ConjModule.map`**, a def, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L174).

> Functoriality of conjugation: a `k`-linear map induces a `k`-linear map of the
> conjugate modules, given by the same underlying function.

```lean
def map (f : M →ₗ[k] N) : ConjModule M →ₗ[k] ConjModule N
```

**`ConjModule.map_apply`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L180).

```lean
lemma map_apply (f : M →ₗ[k] N) (x : ConjModule M) : map f x = f x
```

**`ConjModule.prodEquiv`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L185).

> **Conjugation commutes with finite products.** The conjugate of a product is the product
> of the conjugates, by the identity underlying function: the twisted scalar action is applied
> componentwise.

```lean
def prodEquiv : ConjModule (M × N) ≃ₗ[k] ConjModule M × ConjModule N
```

**`ConjModule.prodEquiv_apply`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L194).

```lean
lemma prodEquiv_apply (x : ConjModule (M × N)) :
    prodEquiv (k := k) x = (map (LinearMap.fst k M N) x, map (LinearMap.snd k M N) x)
```

**`ConjModule.piEquiv`**, a def, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L205).

> **Conjugation commutes with arbitrary products.** The conjugate of a product of a
> family of modules is the product of their conjugates, by the identity underlying
> function: the twisted scalar action is applied componentwise, so no finiteness of the
> index type is needed.

```lean
def piEquiv : ConjModule (∀ i, P i) ≃ₗ[k] ∀ i, ConjModule (P i)
```

**`ConjModule.piEquiv_apply`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L214).

```lean
lemma piEquiv_apply (x : ConjModule (∀ i, P i)) (i : ι) :
    (piEquiv P : ConjModule (∀ i, P i) ≃ₗ[k] ∀ i, ConjModule (P i)) x i
      = map (k := k) (LinearMap.proj i) x
```

**`ConjModule.piEquiv_symm_apply`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L218).

```lean
lemma piEquiv_symm_apply (x : ∀ i, ConjModule (P i)) (i : ι) :
    map (k := k) (LinearMap.proj i)
        ((piEquiv P : ConjModule (∀ i, P i) ≃ₗ[k] ∀ i, ConjModule (P i)).symm x) = x i
```

**`ConjModule.instFinite`**, an instance, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L226).

> The conjugate module of a finite free module is finite: the conjugated basis
> `Basis.conj` is indexed by the same type.

```lean
instance instFinite [Module.Free k M] [Module.Finite k M] :
    Module.Finite k (ConjModule M)
```

**`ConjModule.tensorHom`**, a def, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L232).

> The canonical `k`-linear map `ConjModule M ⊗ ConjModule N → ConjModule (M ⊗ N)`,
> the identity on pure tensors.

```lean
noncomputable def tensorHom : ConjModule M ⊗[k] ConjModule N →ₗ[k] ConjModule (M ⊗[k] N)
```

**`ConjModule.tensorHom_tmul`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L257).

```lean
lemma tensorHom_tmul (m : ConjModule M) (n : ConjModule N) :
    tensorHom (k := k) (m ⊗ₜ[k] n)
      = conjEquiv (k := k) (M := M ⊗[k] N)
        ((conjEquiv (k := k) (M := M)).symm m ⊗ₜ[k] (conjEquiv (k := k) (M := N)).symm n)
```

**`ConjModule.tensorInv`**, a def, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L266).

> The inverse map `ConjModule (M ⊗ N) → ConjModule M ⊗ ConjModule N`, again the identity
> on pure tensors. A `k`-linear map out of `ConjModule X` is the same data as a `k`-linear
> map into `ConjModule` of the target, which is what `map` and `involution` package here.

```lean
noncomputable def tensorInv : ConjModule (M ⊗[k] N) →ₗ[k] ConjModule M ⊗[k] ConjModule N
```

**`ConjModule.tensorEquiv`**, a def, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L294).

> **Conjugation is monoidal.** `ConjModule M ⊗ ConjModule N ≃ₗ[k] ConjModule (M ⊗ N)`,
> the identity on pure tensors. Injectivity comes from `tensorInv` being a left inverse;
> surjectivity from every element of `M ⊗ N` being a sum of pure tensors.

```lean
noncomputable def tensorEquiv :
    ConjModule M ⊗[k] ConjModule N ≃ₗ[k] ConjModule (M ⊗[k] N)
```

**`ConjModule.tensorEquiv_tmul`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L317).

```lean
lemma tensorEquiv_tmul (m : ConjModule M) (n : ConjModule N) :
    tensorEquiv (k := k) (m ⊗ₜ[k] n)
      = conjEquiv (k := k) (M := M ⊗[k] N)
        ((conjEquiv (k := k) (M := M)).symm m ⊗ₜ[k] (conjEquiv (k := k) (M := N)).symm n)
```

**`ConjModule.tensorEquiv_symm_conjEquiv_tmul`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L324).

```lean
lemma tensorEquiv_symm_conjEquiv_tmul (m : M) (n : N) :
    (tensorEquiv (k := k) (M := M) (N := N)).symm
        (conjEquiv (k := k) (M := M ⊗[k] N) (m ⊗ₜ[k] n))
      = conjEquiv (k := k) (M := M) m ⊗ₜ[k] conjEquiv (k := k) (M := N) n
```

## E. Endomorphisms of the conjugate module

> An endomorphism of `M` is read on `ConjModule M` through `conjEquiv`. Conjugating twists
> nothing at the level of the additive group, so the structural identities hold
> definitionally; only the real-scalar one needs an argument.

**`ConjModule.endConj`**, a def, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L345).

> A linear endomorphism read on the conjugate module: the same underlying map,
> through the identity `conjEquiv`. Conjugating twists nothing at the level of the
> additive group, so all structural identities (`comp`, `add`, `neg`, sums) hold
> definitionally.

```lean
def endConj {k : Type*} [CommRing k] [StarRing k] {M : Type*}
    [AddCommGroup M] [Module k M] (f : M →ₗ[k] M) :
    ConjModule M →ₗ[k] ConjModule M
```

**`ConjModule.endConj_apply`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L353).

```lean
lemma endConj_apply {k : Type*} [CommRing k] [StarRing k] {M : Type*}
    [AddCommGroup M] [Module k M] (f : M →ₗ[k] M) (v : ConjModule M) :
    ConjModule.endConj f v =
      conjEquiv (k := k) (M := M) (f ((conjEquiv (k := k) (M := M)).symm v))
```

**`ConjModule.endConj_id`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L358).

```lean
lemma endConj_id {k : Type*} [CommRing k] [StarRing k] {M : Type*}
    [AddCommGroup M] [Module k M] :
    ConjModule.endConj (LinearMap.id : M →ₗ[k] M) = LinearMap.id
```

**`ConjModule.endConj_comp`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L362).

```lean
lemma endConj_comp {k : Type*} [CommRing k] [StarRing k] {M : Type*}
    [AddCommGroup M] [Module k M] (f g : M →ₗ[k] M) :
    ConjModule.endConj (f ∘ₗ g) = ConjModule.endConj f ∘ₗ ConjModule.endConj g
```

**`ConjModule.endConj_add`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L366).

```lean
lemma endConj_add {k : Type*} [CommRing k] [StarRing k] {M : Type*}
    [AddCommGroup M] [Module k M] (f g : M →ₗ[k] M) :
    ConjModule.endConj (f + g) = ConjModule.endConj f + ConjModule.endConj g
```

**`ConjModule.endConj_neg`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L370).

```lean
lemma endConj_neg {k : Type*} [CommRing k] [StarRing k] {M : Type*}
    [AddCommGroup M] [Module k M] (f : M →ₗ[k] M) :
    ConjModule.endConj (-f) = -ConjModule.endConj f
```

**`ConjModule.endConj_multiset_sum`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L374).

```lean
lemma endConj_multiset_sum {k : Type*} [CommRing k] [StarRing k]
    {M : Type*} [AddCommGroup M] [Module k M] (S : Multiset (M →ₗ[k] M)) :
    ConjModule.endConj S.sum = (S.map ConjModule.endConj).sum
```

**`ConjModule.endConj_real_smul`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean#L385).

> Conjugation of endomorphisms commutes with real scalars: the star on the
> conjugated complex scalar is invisible on the reals.

```lean
lemma endConj_real_smul {M : Type*} [AddCommGroup M] [Module ℂ M]
    (r : ℝ) (f : M →ₗ[ℂ] M) :
    ConjModule.endConj (r • f) = r • ConjModule.endConj f
```

## Depends on

- [The conjugate module](../../../../physlib/mathematics/modules/conjmodule.md)

## Sources

- [PhyslibAlpha/Mathematics/Modules/ConjModule.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Modules/ConjModule.lean)
