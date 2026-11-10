---
declaration: section
origin: cited
lean: AlgebraicGeometry.Grassmannian.functor, AlgebraicGeometry.Grassmannian.functor_isRepresentable, AlgebraicGeometry.Grassmannian.scheme, AlgebraicGeometry.Grassmannian.schemeOver, AlgebraicGeometry.Grassmannian.schemeOverRing, Stacks.ProjectiveSpaceModuli.grassmannianSuccIso, Stacks.ProjectiveSpaceModuli.homEquiv_comp_grassmannianSuccIso_hom
statement: formalized
proof: formalized
---

# 27.22 Grassmannians

Section 27.22 of the Stacks Project, [Tag 089R](https://stacks.math.columbia.edu/tag/089R). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 089S, an equation

[Tag 089S](https://stacks.math.columbia.edu/tag/089S) in the Stacks Project.

**`AlgebraicGeometry.Grassmannian.functor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery27/Functor.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery27/Functor.lean#L121).

> The Grassmannian functor `G(k, n)` from schemes to sets, contravariant on morphisms by
> pullback.

```lean
public noncomputable def functor (k n : ℕ) :
    Scheme.{u}ᵒᵖ ⥤ Type u
```

## Tag 089T, a lemma

[Tag 089T](https://stacks.math.columbia.edu/tag/089T) in the Stacks Project.

**`AlgebraicGeometry.Grassmannian.functor_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery27/Representable/Gluing.lean, line 537](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery27/Representable/Gluing.lean#L537). References: SGA 6 VI (4.1), “Grassmannian, free case”.

> The Grassmannian functor `G(k, n)` is representable by a scheme when `0 < k < n`.

```lean
public theorem functor_isRepresentable (k n : ℕ) (hk : 0 < k) (hkn : k < n) :
    (functor.{u} k n).IsRepresentable
```

## Tag 089U, a definition

[Tag 089U](https://stacks.math.columbia.edu/tag/089U) in the Stacks Project.

**`AlgebraicGeometry.Grassmannian.scheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery27/GrassmannianScheme.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery27/GrassmannianScheme.lean#L58). The attribute's comment: “the Grassmannian over ℤ”. References: SGA 6 VI (4.9), “special case”.

> The Grassmannian `G(k, n)` over the integers: the scheme representing the functor of finite
> locally free rank-`n - k` quotients of the free module of rank `n`.

```lean
public def scheme (k n : ℕ) : Scheme.{u}
```

**`AlgebraicGeometry.Grassmannian.schemeOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery27/GrassmannianScheme.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery27/GrassmannianScheme.lean#L72). The attribute's comment: “the Grassmannian over a scheme”. References: SGA 6 VI (4.9); SGA 7 XIX (1.4), “partial”.

> The Grassmannian `G(k, n)_S` over a scheme `S`: the base change of the integral Grassmannian
> along the unique morphism `S ⟶ Spec ℤ`.

```lean
public abbrev schemeOver (k n : ℕ) (S : Scheme.{u}) : Scheme.{u}
```

**`AlgebraicGeometry.Grassmannian.schemeOverRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery27/GrassmannianScheme.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery27/GrassmannianScheme.lean#L97). The attribute's comment: “the Grassmannian over a ring”. References: SGA 6 VI (4.9), “G_S^(n, special case”; SGA 7 XIX (1.4), “partial”.

> The Grassmannian `G(k, n)_R` over a commutative ring `R`: the base change of the integral
> Grassmannian to `Spec R`.

```lean
public abbrev schemeOverRing (k n : ℕ) (R : CommRingCat.{u}) : Scheme.{u}
```

## Tag 089V, a lemma

[Tag 089V](https://stacks.math.columbia.edu/tag/089V) in the Stacks Project.

**`Stacks.ProjectiveSpaceModuli.grassmannianSuccIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpaceModuli/Grassmannian.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpaceModuli/Grassmannian.lean#L357).

> The Grassmannian `G(n, n + 1)` over the integers is isomorphic to projective `n`-space, by
> the comparison of their representations of the functor of finite locally free rank-one quotients
> of the free module of rank `n + 1`.

```lean
def grassmannianSuccIso (n : ℕ) :
    Grassmannian.scheme.{u} n (n + 1) ≅ projectiveSpaceAtUniverse.{u} n
```

**`Stacks.ProjectiveSpaceModuli.homEquiv_comp_grassmannianSuccIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpaceModuli/Grassmannian.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpaceModuli/Grassmannian.lean#L378). The attribute's comment: “the isomorphism matches the two moduli descriptions”.

> The isomorphism `G(n, n + 1) ≅ ℙⁿ_ℤ` matches the two representations: the rank-one quotient
> classified by a morphism `f` to the Grassmannian is classified, after composing with the
> isomorphism, by the same point of the Grassmannian functor read through projective space.

```lean
theorem homEquiv_comp_grassmannianSuccIso_hom (n : ℕ) {Z : Scheme.{u}}
    (f : Z ⟶ Grassmannian.scheme.{u} n (n + 1)) :
    (projectiveSpaceRepresentableBy.{u} n).homEquiv (f ≫ (grassmannianSuccIso.{u} n).hom) =
      (Grassmannian.schemeRepresentableBy.{u} n (n + 1)).homEquiv f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.22, Tag 089R](https://stacks.math.columbia.edu/tag/089R)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
