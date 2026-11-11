---
declaration: section
origin: cited
lean: Module.mittagLeffler_iff_finitePresentation_and_mittagLeffler_of_projective, Module.mittagLeffler_iff_finitePresentation, Module.mittagLeffler_of_projective, Module.mittagLeffler_iff_exists_isLeast_mem_range_rTensor_subtype, Module.flat_and_mittagLeffler_pi, Module.flat_and_mittagLeffler_mvPowerSeries
statement: formalized
proof: formalized
---

# 10.91 Examples and non-examples of Mittag-Leffler modules

Section 10.91 of the Stacks Project, [Tag 059Q](https://stacks.math.columbia.edu/tag/059Q). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 059R, an example

[Tag 059R](https://stacks.math.columbia.edu/tag/059R) in the Stacks Project.

**`Module.mittagLeffler_iff_finitePresentation_and_mittagLeffler_of_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Basic.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/Basic.lean#L336). The attribute's comment: “Items (1) and (3) together, over one module and with the two hypotheses as antecedents; the forms to cite are the two halves. Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 059M, 059N and 059P. Test data in the universe of `M`, whence `Small.{v} R`. See the module docstring.”.

> **Stacks 059R.** Let `R` be a commutative ring and `M` an `R`-module. Then (1) if `M` is
> finitely generated, `M` is Mittag-Leffler if and only if `M` is finitely presented — in particular
> every finitely presented module is Mittag-Leffler — and (2) if `M` is projective, in particular if
> `M` is free, then `M` is Mittag-Leffler. Being Mittag-Leffler is spelled out in the intrinsic form
> 059E (1): every map `f : P → M` from a finitely presented module dominates and is dominated by a
> map `g : P → Q` into a finitely presented module, domination meaning
> `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every `R`-module `N`.
>
> This is the example as the source states it, over one module. The two items are independent of
> each other and each is stated separately, over its own hypothesis alone, as
> `Module.mittagLeffler_iff_finitePresentation` and `Module.mittagLeffler_of_projective`.

```lean
public theorem Module.mittagLeffler_iff_finitePresentation_and_mittagLeffler_of_projective
    (R : Type u) [CommRing R] [Small.{v} R] (M : Type v) [AddCommGroup M] [Module R M] :
    (Module.Finite R M →
        ((∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
            (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
              (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
                [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) ↔
          Module.FinitePresentation R M)) ∧
      (Module.Projective R M →
        ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
          (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
            (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
              [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N))
```

**`Module.mittagLeffler_iff_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Basic.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/Basic.lean#L360). The attribute's comment: “Item (1), with the finite generation an instance hypothesis; `finitely presented implies Mittag-Leffler` is the direction `←`, via `instFiniteOfFinitePresentation`.”.

> **Stacks 059R, item (1).** Let `R` be a commutative ring and `M` a finitely generated
> `R`-module. Then `M` is Mittag-Leffler if and only if `M` is finitely presented; in particular
> every finitely presented module is Mittag-Leffler, finite presentation implying finite generation.
> Being Mittag-Leffler is spelled out in the intrinsic form
> 059E (1): every map `f : P → M` from a finitely presented module dominates and is dominated by a
> map `g : P → Q` into a finitely presented module, domination meaning
> `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every `R`-module `N`.

```lean
public theorem Module.mittagLeffler_iff_finitePresentation (R : Type u) [CommRing R] [Small.{v} R]
    (M : Type v) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    (∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
        (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
          (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
            [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) ↔
      Module.FinitePresentation R M
```

**`Module.mittagLeffler_of_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Basic.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/Basic.lean#L376). The attribute's comment: “Items (2) and (3), with the projectivity an instance hypothesis; item (2), a free module, is this statement via `Module.Projective.of_free`.”.

> **Stacks 059R, items (2) and (3).** Let `R` be a commutative ring and `M` a projective
> `R`-module, in particular a free one, `Module.Projective.of_free` being an instance. Then `M` is
> Mittag-Leffler, spelled out in the intrinsic form 059E (1): every map `f : P → M` from a finitely
> presented module dominates and is dominated by a map `g : P → Q` into a finitely presented module,
> domination meaning `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every `R`-module `N`.

```lean
public theorem Module.mittagLeffler_of_projective (R : Type u) [CommRing R] [Small.{v} R]
    (M : Type v) [AddCommGroup M] [Module R M] [Module.Projective R M] :
    ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
        (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
          (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
            [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)
```

## Tag 059S, a lemma

[Tag 059S](https://stacks.math.columbia.edu/tag/059S) in the Stacks Project.

**`Module.mittagLeffler_iff_exists_isLeast_mem_range_rTensor_subtype`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Flat.lean, line 631](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/Flat.lean#L631). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 059M and 0AS6; `finite free` is `Module.Free` and `Module.Finite`, `x ∈ F' ⊗_R M` is membership in the range of `F'.subtype.rTensor M`, and `smallest` is `IsLeast`. Test data in the universe of `M`, whence `Small.{v} R`. See the module docstring.”.

> Let `R` be a commutative ring and let `M` be a flat `R`-module. Then `M` is Mittag-Leffler if
> and only if for every finite free `R`-module `F` and every `x ∈ F ⊗[R] M` there is a smallest
> submodule `F'` of `F` with `x ∈ F' ⊗[R] M` — that is, with `x` in the range of
> `F' ⊗[R] M → F ⊗[R] M`.
>
> Being Mittag-Leffler is spelled out inline as condition (1) of Proposition 059E: every map
> `f : P → M` from a finitely presented `R`-module dominates and is dominated by a map `g : P → Q`
> into a finitely presented `R`-module, that is `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every
> `R`-module `N`. This is Definition 059F, `IsMittagLeffler`, by `isMittagLeffler_def_iff`.

```lean
public theorem Module.mittagLeffler_iff_exists_isLeast_mem_range_rTensor_subtype (R : Type u)
    [CommRing R] [Small.{v} R] (M : Type v) [AddCommGroup M] [Module R M] [Module.Flat R M] :
    (∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
        (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
          (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
            [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) ↔
      ∀ (F : Type v) [AddCommGroup F] [Module R F] [Module.Free R F] [Module.Finite R F]
        (x : F ⊗[R] M), ∃ F' : Submodule R F,
          IsLeast {N : Submodule R F | x ∈ LinearMap.range (N.subtype.rTensor M)} F'
```

## Tag 05D0, a lemma

[Tag 05D0](https://stacks.math.columbia.edu/tag/05D0) in the Stacks Project.

**`Module.flat_and_mittagLeffler_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Pi.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/Pi.lean#L162). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 059M, 059S and 0AS6; `R^A` is the `Pi` module `A → R`, as in item (3) of 05CZ, and the two conclusions are one conjunction, as in the source. Test data in the universe of `R` and `A`. See the module docstring.”.

> Let `R` be a Noetherian ring and `A` a set. Then `M = R^A`, the `R`-module of functions
> `A → R`, is a flat and Mittag-Leffler `R`-module.
>
> Being Mittag-Leffler is spelled out inline as condition (1) of Proposition 059E: every map
> `f : P → M` from a finitely presented `R`-module dominates and is dominated by a map `g : P → Q`
> into a finitely presented `R`-module, that is `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every
> `R`-module `N`.

```lean
theorem Module.flat_and_mittagLeffler_pi (R : Type u) [CommRing R] [IsNoetherianRing R]
    (A : Type u) :
    Module.Flat R (A → R) ∧
      ∀ (P : Type u) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
        (f : P →ₗ[R] (A → R)), ∃ (Q : Type u) (_ : AddCommGroup Q) (_ : Module R Q)
          (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type u) [AddCommGroup N]
            [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)
```

## Tag 059T, a lemma

[Tag 059T](https://stacks.math.columbia.edu/tag/059T) in the Stacks Project.

**`Module.flat_and_mittagLeffler_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/MvPowerSeries.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/MvPowerSeries.lean#L127). The attribute's comment: “The source's `0 < n` is dropped as unused: at `n = 0` the module is free of rank one, hence flat and Mittag-Leffler. Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 05D0, 059M, 059S and 0AS6; `R[[t_1, …, t_n]]` is `MvPowerSeries (Fin n) R`, the product over the monomials with its coefficientwise `R`-module structure, and the two conclusions are one conjunction, as in the source. Test data in the universe of `R`. See the module docstring.”.

> Let `R` be a Noetherian ring and let `n : ℕ`. Then the power series module
> `M = R[[t_1, …, t_n]]`, regarded as an `R`-module, is flat and Mittag-Leffler.
>
> Being Mittag-Leffler is spelled out inline as condition (1) of Proposition 059E: every map
> `f : P → M` from a finitely presented `R`-module dominates and is dominated by a map `g : P → Q`
> into a finitely presented `R`-module, that is `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every
> `R`-module `N`.

```lean
theorem Module.flat_and_mittagLeffler_mvPowerSeries (R : Type u) [CommRing R]
    [IsNoetherianRing R] (n : ℕ) :
    Module.Flat R (MvPowerSeries (Fin n) R) ∧
      ∀ (P : Type u) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
        (f : P →ₗ[R] MvPowerSeries (Fin n) R), ∃ (Q : Type u) (_ : AddCommGroup Q)
          (_ : Module R Q) (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q),
            ∀ (N : Type u) [AddCommGroup N] [Module R N],
              LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.91, Tag 059Q](https://stacks.math.columbia.edu/tag/059Q)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
