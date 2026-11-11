---
declaration: section
origin: cited
lean: StacksDraft.ProjectiveDimension.HasProjectiveAmplitude, StacksDraft.ProjectiveDimension.HasFiniteProjectiveDimension, StacksDraft.ProjectiveDimension.hasProjectiveAmplitude_iff_ext_vanishing, StacksDraft.ProjectiveDimension.dualNumber_quotient_eps_periodic_resolution_infinite_dimension
statement: formalized
proof: formalized
---

# 15.70 Projective dimension

Section 15.70 of the Stacks Project, [Tag 0A5M](https://stacks.math.columbia.edu/tag/0A5M). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A5N, a definition

[Tag 0A5N](https://stacks.math.columbia.edu/tag/0A5N) in the Stacks Project.

**`StacksDraft.ProjectiveDimension.HasProjectiveAmplitude`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ProjectiveDimension/Amplitude.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/ProjectiveDimension/Amplitude.lean#L48). The attribute's comment: “projective amplitude”.

> An object of `D(R)` has **projective amplitude in `[a, b]`** if it is represented by a
> complex of projective `R`-modules whose terms vanish outside degrees `a` through `b`.

```lean
public def HasProjectiveAmplitude
    (K : DerivedCategory (ModuleCat.{v} R)) (a b : ℤ) : Prop
```

**`StacksDraft.ProjectiveDimension.HasFiniteProjectiveDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ProjectiveDimension/Amplitude.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/ProjectiveDimension/Amplitude.lean#L58). The attribute's comment: “finite projective dimension”.

> An object of `D(R)` has **finite projective dimension** if it is represented by a bounded
> complex of projective `R`-modules.

```lean
public def HasFiniteProjectiveDimension
    (K : DerivedCategory (ModuleCat.{v} R)) : Prop
```

## Tag 0A5P, a lemma

[Tag 0A5P](https://stacks.math.columbia.edu/tag/0A5P) in the Stacks Project.

**`StacksDraft.ProjectiveDimension.hasProjectiveAmplitude_iff_ext_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ProjectiveDimension/Criteria.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/ProjectiveDimension/Criteria.lean#L464).

> **Stacks 0A5P.** Projective amplitude in `[a, b]` is equivalent to vanishing of all Ext
> groups outside degrees `[-b, -a]`; equivalently, it can be detected using upper cohomology
> vanishing and Ext groups above degree `-a`, or using cohomology outside `[a - 1, b]` and the
> single Ext degree `-a + 1`.

```lean
public theorem hasProjectiveAmplitude_iff_ext_vanishing [Small.{v} R]
    (K : DerivedCategory (ModuleCat.{v} R)) (a b : ℤ) :
    let moduleObject := fun N : ModuleCat.{v} R ↦
      (DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj N
    let projectiveAmplitude := HasProjectiveAmplitude K a b
    let extOutsideVanishes := ∀ (N : ModuleCat.{v} R) (i : ℤ),
      i ∉ Set.Icc (-b) (-a) → Subsingleton (DerivedCategory.Ext K (moduleObject N) i)
    let upperVanishing :=
      (∀ n : ℤ, b < n → IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) n).obj K)) ∧
        ∀ (N : ModuleCat.{v} R) (i : ℤ), -a < i →
          Subsingleton (DerivedCategory.Ext K (moduleObject N) i)
    let endpointVanishing :=
      (∀ n : ℤ, n ∉ Set.Icc (a - 1) b →
        IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) n).obj K)) ∧
        ∀ N : ModuleCat.{v} R,
          Subsingleton (DerivedCategory.Ext K (moduleObject N) (-a + 1))
    (projectiveAmplitude ↔ extOutsideVanishes) ∧
      (extOutsideVanishes ↔ upperVanishing) ∧
      (upperVanishing ↔ endpointVanishing)
```

## Tag 0A5Q, an example

[Tag 0A5Q](https://stacks.math.columbia.edu/tag/0A5Q) in the Stacks Project.

**`StacksDraft.ProjectiveDimension.dualNumber_quotient_eps_periodic_resolution_infinite_dimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ProjectiveDimension/DualNumbers.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/ProjectiveDimension/DualNumbers.lean#L277).

> **Stacks 0A5Q.** For the ring `R = k[ε]` of dual numbers over a field and `M = R/(ε)`, the
> module `M` is represented by the periodic free complex with all differentials multiplication by
> `ε`, but `M` has infinite projective dimension.

```lean
public theorem dualNumber_quotient_eps_periodic_resolution_infinite_dimension
    (k : Type u) [Field k]
    [HasDerivedCategory.{w} (ModuleCat.{u} (DualNumber k))] :
    let R := DualNumber k
    let ε : R := DualNumber.eps
    let M := ModuleCat.of R (R ⧸ Ideal.span {ε})
    projectiveDimension M = ⊤ ∧
      ∃ P : CochainComplex (ModuleCat.{u} R) ℤ,
        Nonempty
          (DerivedCategory.Q.obj P ≅
            (DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj M) ∧
          (∀ i : ℤ, 0 < i → IsZero (P.X i)) ∧
          ∃ e : ∀ n : ℕ, P.X (-(n : ℤ)) ≅ ModuleCat.of R R,
            ∀ n : ℕ,
              P.d (-((n + 1 : ℕ) : ℤ)) (-(n : ℤ)) ≫ (e n).hom =
                (e (n + 1)).hom ≫
                  ModuleCat.ofHom (LinearMap.mulLeft R ε)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.70, Tag 0A5M](https://stacks.math.columbia.edu/tag/0A5M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
