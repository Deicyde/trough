---
declaration: section
origin: cited
lean: Stacks.CechKunneth.kunnethIsoOfAffineDiagonal_eq, Stacks.CechKunneth.kunnethIsoOfAffineDiagonal, AlgebraicGeometry.nonempty_kunnethIso_of_isAffineHom_diagonal, AlgebraicGeometry.KunnethQcqs.isIso_kunnethMap
statement: formalized
proof: formalized
---

# 33.29 Künneth formula, I

Section 33.29 of the Stacks Project, [Tag 0BEC](https://stacks.math.columbia.edu/tag/0BEC). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BED, a lemma

[Tag 0BED](https://stacks.math.columbia.edu/tag/0BED) in the Stacks Project.

**`Stacks.CechKunneth.kunnethIsoOfAffineDiagonal_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/CechKunneth/KunnethCanonical.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/CechKunneth/KunnethCanonical.lean#L139). The attribute's comment: “the isomorphism is canonical: independent of the chosen finite affine covers, and on Cech classes given by the cup product of the pulled-back cocycles”.

> **The Künneth isomorphism is canonical**: it is the isomorphism
> `Stacks.CechKunneth.kunnethIsoOfCovers` of *any* pair of finite affine coverings of `X` and `Y`,
> which on Čech classes is the Alexander–Whitney product of the pulled-back cocycles
> (`Stacks.CechKunneth.kunnethIsoOfCovers_symm_lof_tmul`).

```lean
theorem kunnethIsoOfAffineDiagonal_eq [CompactSpace X] [CompactSpace Y] (n : ℕ) :
    kunnethIsoOfAffineDiagonal k f g F G n = kunnethIsoOfCovers f g CX CY F G n
```

**`Stacks.CechKunneth.kunnethIsoOfAffineDiagonal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/CechKunneth/KunnethFormula.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/CechKunneth/KunnethFormula.lean#L376). The attribute's comment: “for X and Y quasi-compact with affine diagonal over a field k and F, G quasi-coherent: H^n(X x\_k Y, pr\_1^*F (x) pr\_2^*G) is the direct sum over p + q = n of H^p(X, F) (x)\_k H^q(Y, G), the isomorphism being the Cech-level cup product of pulled-back cocycles”.

> **The Künneth formula** [Stacks, Tag 0BED]. For a field `k`, quasi-compact schemes `X` and `Y`
> over `k` with affine diagonal, a quasi-coherent `𝒪_X`-module `ℱ` and a quasi-coherent
> `𝒪_Y`-module `𝒢`,
> `Hⁿ(X ×_k Y, pr₁^*ℱ ⊗_{𝒪_{X ×_k Y}} pr₂^*𝒢) ≅ ⨁_{p + q = n} Hᵖ(X, ℱ) ⊗_k H^q(Y, 𝒢)`.
>
> The isomorphism is the one of the source: computed on finite affine coverings `𝒰` of `X` and `𝒱`
> of `Y` (chosen by `Stacks.CechKunneth.finiteAffineCover`), it carries the class of the
> Alexander–Whitney product of the pullbacks of two Čech cocycles — the Čech form of
> `pr₁^*α ∪ pr₂^*β`, [Stacks, Tag 0BEE] — to `α ⊗ β`; see
> `Stacks.CechKunneth.kunnethIsoOfCovers_symm_lof_tmul`. The cohomology groups are Mathlib's right
> derived functors of global sections, regarded as `k`-modules through the structure morphisms
> (`Stacks.CechKunneth.cohomologyK`).

```lean
def kunnethIsoOfAffineDiagonal [CompactSpace X] [CompactSpace Y] (n : ℕ) :
    cohomologyK (pullback.fst f g ≫ f) (externalTensorProduct f g F G) n ≃ₗ[k]
      DirectSum {pq : ℕ × ℕ // pq.1 + pq.2 = n}
        (fun pq => cohomologyK f F pq.1.1 ⊗[k] cohomologyK g G pq.1.2)
```

**`AlgebraicGeometry.nonempty_kunnethIso_of_isAffineHom_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Varieties/KunnethAffineDiagonal.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Varieties/KunnethAffineDiagonal.lean#L71). The attribute's comment: “for X and Y quasi-compact with affine diagonal over a field k and F, G quasi-coherent: H^n(X x\_k Y, pr\_1^*F (x) pr\_2^*G) is isomorphic to the direct sum over p + q = n of H^p(X, F) (x)\_k H^q(Y, G)”.

> **The Künneth formula.** For quasi-coherent modules `F` on `X` and `G` on `Y`, with `X` and
> `Y` quasi-compact schemes over a field `k` whose diagonals are affine, the cohomology of the
> external tensor product `pr₁^*F ⊗ pr₂^*G` on `X ×_{Spec k} Y` is isomorphic to the direct sum of
> the tensor products `Hᵖ(X, F) ⊗_k Hᑫ(Y, G)` over the pairs with `p + q = n`.

```lean
theorem nonempty_kunnethIso_of_isAffineHom_diagonal
    (k : Type u) [Field k] {X Y : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    [CompactSpace X] [IsAffineHom (pullback.diagonal (terminal.from X))]
    [CompactSpace Y] [IsAffineHom (pullback.diagonal (terminal.from Y))]
    (F : X.Modules) (G : Y.Modules) [F.IsQuasicoherent] [G.IsQuasicoherent] (n : ℕ) :
    Nonempty
      (cohomologyOverField k (pullback.fst f g ≫ f) (externalTensorSheaf f g F G) n ≅
        ModuleCat.of k
          (⨁ pq : {pq : ℕ × ℕ // pq.1 + pq.2 = n},
            TensorProduct k (cohomologyOverField k f F pq.1.1)
              (cohomologyOverField k g G pq.1.2)))
```

## Tag 0BEF, a lemma

[Tag 0BEF](https://stacks.math.columbia.edu/tag/0BEF) in the Stacks Project.

**`AlgebraicGeometry.KunnethQcqs.isIso_kunnethMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Varieties/KunnethQcqs.lean, line 484](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Varieties/KunnethQcqs.lean#L484). The attribute's comment: “the canonical Künneth map, an isomorphism in every degree n”.

> **[Stacks, Tag 0BEF], the Künneth formula.** Let `k` be a field, let `X` and `Y` be schemes
> over `k` and let `F`, `G` be quasi-coherent modules on `X`, `Y`. If `X` and `Y` are quasi-compact
> and quasi-separated, the canonical map
>
> `⨁_{p + q = n} Hᵖ(X, F) ⊗_k Hᑫ(Y, G) ⟶ Hⁿ(X ×_{Spec k} Y, pr₁^*F ⊗_{𝒪_{X ×_k Y}} pr₂^*G)`
>
> of `AlgebraicGeometry.KunnethQcqs.kunnethMap` is an isomorphism for every `n`; its inverse is
> `AlgebraicGeometry.KunnethQcqs.kunnethIso`. This is the library's registration of the tag: the
> untagged `AlgebraicGeometry.nonempty_kunnethIso` reaches an abstract isomorphism from a datum of
> derived global sections instead.

```lean
theorem isIso_kunnethMap [CompactSpace Y] [QuasiSeparatedSpace Y] :
    IsIso (kunnethMap f g F G n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.29, Tag 0BEC](https://stacks.math.columbia.edu/tag/0BEC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
