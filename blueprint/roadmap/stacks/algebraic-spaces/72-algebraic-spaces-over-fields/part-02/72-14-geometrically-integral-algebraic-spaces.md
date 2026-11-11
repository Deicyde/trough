---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsGeometricallyIntegral, AlgebraicGeometry.Space.isGeometricallyIntegral_iff, AlgebraicGeometry.Space.finiteDimensional_globalFunctions_of_isProper, AlgebraicGeometry.Space.finite_connectedComponents_points_of_isProper, AlgebraicGeometry.Space.nonempty_componentwiseArtinianFactorization_of_isProper, AlgebraicGeometry.Space.isField_componentFunctions, AlgebraicGeometry.Space.finiteDimensional_componentFunctions_of_isProper, AlgebraicGeometry.Space.nonempty_componentwiseArtinianFactorization_of_isProper_of_field
statement: formalized
proof: formalized
---

# 72.14 Geometrically integral algebraic spaces

Section 72.14 of the Stacks Project, [Tag 0DMV](https://stacks.math.columbia.edu/tag/0DMV). 4 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DMW, a definition

[Tag 0DMW](https://stacks.math.columbia.edu/tag/0DMW) in the Stacks Project.

**`AlgebraicGeometry.Space.IsGeometricallyIntegral`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyIntegral.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyIntegral.lean#L102).

> **Stacks 0DMW.** An algebraic space over a field `k` is *geometrically integral* when its
> base change to every field extension of `k` is an integral algebraic space.

```lean
def IsGeometricallyIntegral (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u) : Prop
```

## Tag 0DMX, a lemma

[Tag 0DMX](https://stacks.math.columbia.edu/tag/0DMX) in the Stacks Project.

**`AlgebraicGeometry.Space.isGeometricallyIntegral_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyIntegral.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyIntegral.lean#L169).

> **Stacks 0DMX.** A decent algebraic space over a field `k` is geometrically integral over
> `k` exactly when it is geometrically reduced and geometrically irreducible over `k`.

```lean
theorem isGeometricallyIntegral_iff (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (hdecent : IsDecentSpace B (Spec (.of k)) hk X) :
    IsGeometricallyIntegral B k hk X ↔
      IsGeometricallyReduced k B hk X hX ∧ IsGeometricallyIrreducible B k hk X
```

## Tag 0DMY, a lemma

[Tag 0DMY](https://stacks.math.columbia.edu/tag/0DMY) in the Stacks Project.

**`AlgebraicGeometry.Space.finiteDimensional_globalFunctions_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctions.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctions.lean#L306). The attribute's comment: “part (1), with Stacks 08AS — finiteness over the base ring of the cohomology of a coherent module on a proper algebraic space, in every degree — carried as the hypothesis h08AS”.

> **Stacks 0DMY, part (1).**  The global regular functions of a proper algebraic space `X`
> over a field `k` form a finite dimensional `k`-algebra.
>
> Tag 0DMY gets this from Tag 08AS, which is carried here as the hypothesis `h08AS`:  the
> cohomology over `k` of every coherent `𝒪_X`-module is a finite `k`-module in every degree.
> Properness makes `X` locally Noetherian over `k`, so the structure sheaf is a coherent
> `𝒪_X`-module by `AlgebraicGeometry.Space.isCoherent_structureModuleLarge`, and its degree-zero
> cohomology over `k` is the ring of global functions by
> `AlgebraicGeometry.Space.cohomologyZeroStructureModuleLinearEquiv`.

```lean
theorem finiteDimensional_globalFunctions_of_isProper (hf : IsProper B (Spec (.of k)) hS f)
    (h08AS : ∀ M : Modules.{u, u + 1} B (Spec (.of k)) hS X hX,
      IsCoherent B (Spec (.of k)) hS X hX M → ∀ i : ℕ,
        Module.Finite k (cohomologyOverBase.{u, u} k B hS X hX M i)) :
    Module.Finite k (globalFunctions B (Spec (.of k)) hS X)
```

**`AlgebraicGeometry.Space.finite_connectedComponents_points_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctions.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctions.lean#L336). The attribute's comment: “part (2): the product is finite, there being one factor for each of the finitely many connected components of the point space”.

> **Stacks 0DMY, part (2), the number of factors.**  The point space of a proper algebraic
> space over a field has finitely many connected components, so that the product decomposition of
> its global regular functions is a finite product.
>
> Properness makes `X` quasi-compact and locally Noetherian through Tags 04ZL and 04ZK, and
> Tag 04ZF then makes `|X|` a Noetherian topological space;  a Noetherian space has finitely many
> connected components.  Tag 08AS is not used.

```lean
theorem finite_connectedComponents_points_of_isProper (hf : IsProper B (Spec (.of k)) hS f) :
    Finite (ConnectedComponents (points B (Spec (.of k)) hS X))
```

**`AlgebraicGeometry.Space.nonempty_componentwiseArtinianFactorization_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctions.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctions.lean#L358). The attribute's comment: “part (2), with Stacks 08AS — finiteness over the base ring of the cohomology of a coherent module on a proper algebraic space, in every degree — carried as the hypothesis h08AS”.

> **Stacks 0DMY, part (2).**  The global regular functions of a proper algebraic space over a
> field split as the product, over the connected components of its point space, of the rings of
> functions on the étale charts lying in each component;  each factor is an Artinian local ring,
> and the splitting is simultaneous restriction to the components.  The set of components is
> finite by `AlgebraicGeometry.Space.finite_connectedComponents_points_of_isProper`, so the
> product is finite.
>
> This is `AlgebraicGeometry.Space.nonempty_componentwiseArtinianFactorization_of_isQuasiCompactSpace`
> with its remaining hypothesis discharged:  artinianness of the whole ring of global functions
> is `AlgebraicGeometry.Space.isArtinianRing_globalFunctions_of_isProper`, hence part (1) of
> Tag 0DMY.  Quasi-compactness and local Noetherianity of `X` come from properness through
> Tags 04ZL and 04ZK, and Tag 04ZF then makes the point space Noetherian, so that the set of
> connected components is finite.

```lean
theorem nonempty_componentwiseArtinianFactorization_of_isProper
    (hf : IsProper B (Spec (.of k)) hS f)
    (h08AS : ∀ M : Modules.{u, u + 1} B (Spec (.of k)) hS X hX,
      IsCoherent B (Spec (.of k)) hS X hX M → ∀ i : ℕ,
        Module.Finite k (cohomologyOverBase.{u, u} k B hS X hX M i)) :
    Nonempty (ComponentwiseArtinianFactorization k B hS X)
```

**`AlgebraicGeometry.Space.isField_componentFunctions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctions.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctions.lean#L408). The attribute's comment: “part (3): the factors of a reduced space are fields”.

> **Stacks 0DMY, part (3).**  For a reduced algebraic space, each factor of a componentwise
> factorization of its global regular functions is a field:  the factor is an Artinian local ring
> by the factorization and reduced by
> `AlgebraicGeometry.Space.isReduced_componentFunctions`, and a reduced Artinian local ring is a
> field.

```lean
theorem isField_componentFunctions
    (hred : HasEtaleLocalProperty B (Spec (.of k)) hS X
      (fun T : Scheme.{u} => _root_.AlgebraicGeometry.IsReduced T))
    (fac : ComponentwiseArtinianFactorization k B hS X)
    (c : ConnectedComponents (points B (Spec (.of k)) hS X)) :
    IsField (componentFunctions B (Spec (.of k)) hS X c)
```

**`AlgebraicGeometry.Space.finiteDimensional_componentFunctions_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctions.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctions.lean#L430). The attribute's comment: “part (3): the factors are finite over the base field, with Stacks 08AS — finiteness over the base ring of the cohomology of a coherent module on a proper algebraic space, in every degree — carried as the hypothesis h08AS”.

> **Stacks 0DMY, part (3).**  Each factor of a componentwise factorization of the global
> regular functions of a proper algebraic space over a field is finite dimensional over that
> field — so that, `X` being reduced, each factor is a finite field extension of `k` by
> `AlgebraicGeometry.Space.isField_componentFunctions`.
>
> The global functions are finite dimensional by part (1), the factorization makes the product of
> the factors `k`-linearly isomorphic to them, and projection onto a factor is a surjective
> `k`-linear map.  Reducedness is not used.

```lean
theorem finiteDimensional_componentFunctions_of_isProper (hf : IsProper B (Spec (.of k)) hS f)
    (h08AS : ∀ M : Modules.{u, u + 1} B (Spec (.of k)) hS X hX,
      IsCoherent B (Spec (.of k)) hS X hX M → ∀ i : ℕ,
        Module.Finite k (cohomologyOverBase.{u, u} k B hS X hX M i))
    (fac : ComponentwiseArtinianFactorization k B hS X)
    (c : ConnectedComponents (points B (Spec (.of k)) hS X)) :
    @Module.Finite k (componentFunctions B (Spec (.of k)) hS X c) _ _
      (@Algebra.toModule k (componentFunctions B (Spec (.of k)) hS X c) _ _
        (fac.factorAlgebra c))
```

**`AlgebraicGeometry.Space.nonempty_componentwiseArtinianFactorization_of_isProper_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsFinite.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsFinite.lean#L101). The attribute's comment: “part (2): A is the product, over the connected components of |X|, of Artinian local k-algebras, the splitting being restriction to the components”.

> **Stacks 0DMY, part (2).**  The global regular functions `A` of a proper algebraic space over
> a field `k` split as the product, over the connected components of the point space `|X|`, of the
> rings of functions on the étale charts lying in each component, each factor an Artinian local
> `k`-algebra, the splitting being simultaneous restriction to the components; there are finitely
> many components (`AlgebraicGeometry.Space.finite_connectedComponents_points_of_isProper`), so the
> product is finite.
>
> This is
> `AlgebraicGeometry.Space.nonempty_componentwiseArtinianFactorization_of_isQuasiCompactSpace`
> with its remaining hypothesis, artinianness of `A`, supplied by part (1):
> `AlgebraicGeometry.Space.isArtinianRing_globalFunctions_of_isProper_of_field`.
> Quasi-compactness and local Noetherianity of `X` come from properness (Tags 04ZL and 04ZK).

```lean
theorem nonempty_componentwiseArtinianFactorization_of_isProper_of_field
    (hf : IsProper B (Spec (.of k)) hS f) :
    Nonempty (ComponentwiseArtinianFactorization k B hS X)
```

**`AlgebraicGeometry.Space.moduleFinite_componentFunctions_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsFinite.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsFinite.lean#L118). The attribute's comment: “part (3): the factors are finite over the base field”.

> **Stacks 0DMY, part (3), finiteness of the factors.**  Each factor of a componentwise
> factorization of the global regular functions of a proper algebraic space over a field `k` is
> finite dimensional over `k` — so that, `X` being reduced, each factor is a field
> (`AlgebraicGeometry.Space.isField_componentFunctions`) finite over `k`.
>
> The global functions are finite dimensional by part (1), the factorization makes the product of
> the factors `k`-linearly isomorphic to them, and projection onto a factor is a surjective
> `k`-linear map.

```lean
theorem moduleFinite_componentFunctions_of_isProper (hf : IsProper B (Spec (.of k)) hS f)
    (fac : ComponentwiseArtinianFactorization k B hS X)
    (c : ConnectedComponents (points B (Spec (.of k)) hS X)) :
    @Module.Finite k (componentFunctions B (Spec (.of k)) hS X c) _ _
      (@Algebra.toModule k (componentFunctions B (Spec (.of k)) hS X c) _ _
        (fac.factorAlgebra c))
```

**`AlgebraicGeometry.Space.exists_componentwiseArtinianFactorization_isField_finite_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsFinite.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsFinite.lean#L140). The attribute's comment: “part (3)”.

> **Stacks 0DMY, part (3).**  Let `X` be a reduced proper algebraic space over a field `k`.
> Then `A = H⁰(X, 𝒪_X)` is a product of fields, each a finite extension of `k`: there is a
> componentwise factorization of `A` (part (2)), and each of its factors is a field
> (`AlgebraicGeometry.Space.isField_componentFunctions`, the factor being reduced by Tag 0BGS and
> Artinian local) which is finite dimensional over `k`
> (`AlgebraicGeometry.Space.moduleFinite_componentFunctions_of_isProper`).

```lean
theorem exists_componentwiseArtinianFactorization_isField_finite_of_isProper
    (hf : IsProper B (Spec (.of k)) hS f)
    (hred : HasEtaleLocalProperty B (Spec (.of k)) hS X
      (fun T : Scheme.{u} => _root_.AlgebraicGeometry.IsReduced T)) :
    ∃ fac : ComponentwiseArtinianFactorization k B hS X,
      ∀ c : ConnectedComponents (points B (Spec (.of k)) hS X),
        IsField (componentFunctions B (Spec (.of k)) hS X c) ∧
          @Module.Finite k (componentFunctions B (Spec (.of k)) hS X c) _ _
            (@Algebra.toModule k (componentFunctions B (Spec (.of k)) hS X c) _ _
              (fac.factorAlgebra c))
```

**`AlgebraicGeometry.Space.isSeparable_componentFunctions_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsGeometric.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsGeometric.lean#L91). The attribute's comment: “part (4): if X is geometrically reduced, each factor k\_i is finite separable over k”.

> **Stacks 0DMY, part (4).**  For a proper *geometrically* reduced algebraic space `X` over a
> field `k`, each factor `k_i` of the global regular functions `A = ∏ k_i` is a finite separable
> field extension of `k`:  for every componentwise factorization of `A` (part (2)) and every
> connected component `c` of `|X|`, the factor at `c` is a field, finite over `k` and separable
> over `k`.

```lean
theorem isSeparable_componentFunctions_of_isProper (hf : IsProper B (Spec (.of k)) hS f)
    (hgr : IsGeometricallyReduced k B hS X hX)
    (fac : ComponentwiseArtinianFactorization k B hS X)
    (c : ConnectedComponents (points B (Spec (.of k)) hS X)) :
    IsField (componentFunctions B (Spec (.of k)) hS X c) ∧
      @Module.Finite k (componentFunctions B (Spec (.of k)) hS X c) _ _
        (@Algebra.toModule k (componentFunctions B (Spec (.of k)) hS X c) _ _
          (fac.factorAlgebra c)) ∧
      @Algebra.IsSeparable k (componentFunctions B (Spec (.of k)) hS X c) _ _
        (fac.factorAlgebra c)
```

**`AlgebraicGeometry.Space.irreducibleSpace_primeSpectrum_globalFunctions_tensorProduct_of_isGeometricallyConnected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsGeometric.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsGeometric.lean#L110). The attribute's comment: “part (5): if X is geometrically connected, A is geometrically irreducible over k”.

> **Stacks 0DMY, part (5).**  For a proper geometrically connected algebraic space `X` over a
> field `k`, the ring `A = H⁰(X, 𝒪_X)` of global regular functions is geometrically irreducible
> over `k`:  the spectrum of `A ⊗_k K` is irreducible for every field extension `K/k`.

```lean
theorem irreducibleSpace_primeSpectrum_globalFunctions_tensorProduct_of_isGeometricallyConnected
    (hf : IsProper B (Spec (.of k)) hS f) (hconn : IsGeometricallyConnected B k hS X) :
    ∀ (K : Type v) [Field K] [Algebra k K],
      IrreducibleSpace (PrimeSpectrum (globalFunctions B (Spec (.of k)) hS X ⊗[k] K))
```

**`AlgebraicGeometry.Space.irreducibleSpace_primeSpectrum_globalFunctions_tensorProduct_of_isGeometricallyIrreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsGeometric.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsGeometric.lean#L127). The attribute's comment: “part (6): if X is geometrically irreducible, A is geometrically irreducible over k”.

> **Stacks 0DMY, part (6).**  For a proper geometrically irreducible algebraic space `X` over
> a field `k`, the ring `A = H⁰(X, 𝒪_X)` of global regular functions is geometrically irreducible
> over `k`.
>
> As in the source, this is part (5): every base change of `X` has an irreducible, hence
> connected, point space.

```lean
theorem irreducibleSpace_primeSpectrum_globalFunctions_tensorProduct_of_isGeometricallyIrreducible
    (hf : IsProper B (Spec (.of k)) hS f) (hirr : IsGeometricallyIrreducible B k hS X) :
    ∀ (K : Type v) [Field K] [Algebra k K],
      IrreducibleSpace (PrimeSpectrum (globalFunctions B (Spec (.of k)) hS X ⊗[k] K))
```

**`AlgebraicGeometry.Space.bijective_baseToGlobalFunctions_of_isGeometricallyConnected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsGeometric.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsGeometric.lean#L141). The attribute's comment: “part (7): if X is geometrically reduced and (geometrically) connected, A = k”.

> **Stacks 0DMY, part (7).**  For a proper geometrically reduced and geometrically connected
> algebraic space `X` over a field `k`, the canonical homomorphism `k ⟶ H⁰(X, 𝒪_X)` is bijective:
> `A = k`.

```lean
theorem bijective_baseToGlobalFunctions_of_isGeometricallyConnected
    (hf : IsProper B (Spec (.of k)) hS f) (hgr : IsGeometricallyReduced k B hS X hX)
    (hconn : IsGeometricallyConnected B k hS X) :
    Function.Bijective (baseToGlobalFunctions k B hS X)
```

**`AlgebraicGeometry.Space.bijective_baseToGlobalFunctions_of_isGeometricallyIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsGeometric.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsGeometric.lean#L156). The attribute's comment: “part (8): if X is geometrically integral, A = k”.

> **Stacks 0DMY, part (8).**  For a proper geometrically integral algebraic space `X` over a
> field `k`, the canonical homomorphism `k ⟶ H⁰(X, 𝒪_X)` is bijective:  `A = k`.
>
> As in the source, this is part (7):  a geometrically integral algebraic space is geometrically
> reduced and geometrically connected.

```lean
theorem bijective_baseToGlobalFunctions_of_isGeometricallyIntegral
    (hf : IsProper B (Spec (.of k)) hS f) (hint : IsGeometricallyIntegral B k hS X) :
    Function.Bijective (baseToGlobalFunctions k B hS X)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.moduleFinite_globalFunctions_of_isProper`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalSections/Finiteness.lean#L341), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsFinite.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGlobalFunctionsFinite.lean#L53) (StacksFrontier): “part (1): A is finite over the base, here any Noetherian ring”.

## Tag 0DMZ, a lemma

[Tag 0DMZ](https://stacks.math.columbia.edu/tag/0DMZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isTrivial_of_nontrivial_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvertibleModuleTriviality.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/InvertibleModuleTriviality.lean#L423). The attribute's comment: “granted that H⁰(F, 𝒪\_F) is a field, which Tag 0DMY draws from properness”.

> **Stacks 0DMZ.**  Let `F` be an integral algebraic space whose ring `H⁰(F, 𝒪_F)` of global
> regular functions is a field, and let `L` be an invertible `𝒪_F`-module.  If `H⁰(F, L)` and
> `H⁰(F, L^{⊗ -1})` are both nonzero then `L ≅ 𝒪_F`.
>
> The source states this for a proper integral algebraic space over a field `k`, and uses
> properness only through Tag 0DMY, that `H⁰(F, 𝒪_F)` is then a field.  That result is not
> available in this library, so it is carried here as the hypothesis `hfield`; the base is
> correspondingly an arbitrary scheme rather than the spectrum of a field.

```lean
theorem isTrivial_of_nontrivial_sections (hint : IsIntegralSpace B S hS F)
    (hfield : IsField (globalFunctions B S hS F))
    (L : SheafOfModules.{u} (modulesRingSheaf B S hS F hF))
    [IsInvertible (structureSheaf B S hS F hF).obj (structureRingPresheaf_isSheaf B S hS F hF) L]
    (hL : Nontrivial L.sections)
    (hLinv : Nontrivial (tensorPower (structureSheaf B S hS F hF).obj
      (structureRingPresheaf_isSheaf B S hS F hF) L (-1)).sections) :
    IsTrivial (structureSheaf B S hS F hF).obj (structureRingPresheaf_isSheaf B S hS F hF) L
```

**`AlgebraicGeometry.Space.isTrivial_of_nontrivial_sections_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperIntegralInvertibleTriviality.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperIntegralInvertibleTriviality.lean#L140).

> **Stacks 0DMZ.**  Let `k` be a field, let `X` be a proper integral algebraic space over `k`
> and let `L` be an invertible `𝒪_X`-module.  If `H⁰(X, L)` and `H⁰(X, L^{⊗ -1})` are both
> nonzero then `L ≅ 𝒪_X`.
>
> This is `AlgebraicGeometry.Space.isTrivial_of_nontrivial_sections` with its hypothesis that
> `H⁰(X, 𝒪_X)` be a field discharged from properness and integrality by
> `AlgebraicGeometry.Space.isField_globalFunctions_of_isProper_of_isIntegralSpace`.

```lean
theorem isTrivial_of_nontrivial_sections_of_isProper
    (hf : IsProper B (Spec (.of k)) hS f)
    (hint : IsIntegralSpace B (Spec (.of k)) hS X)
    (L : SheafOfModules.{u} (modulesRingSheaf B (Spec (.of k)) hS X hX))
    [IsInvertible (structureSheaf B (Spec (.of k)) hS X hX).obj
      (structureRingPresheaf_isSheaf B (Spec (.of k)) hS X hX) L]
    (hL : Nontrivial L.sections)
    (hLinv : Nontrivial (tensorPower (structureSheaf B (Spec (.of k)) hS X hX).obj
      (structureRingPresheaf_isSheaf B (Spec (.of k)) hS X hX) L (-1)).sections) :
    IsTrivial (structureSheaf B (Spec (.of k)) hS X hX).obj
      (structureRingPresheaf_isSheaf B (Spec (.of k)) hS X hX) L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.14, Tag 0DMV](https://stacks.math.columbia.edu/tag/0DMV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
