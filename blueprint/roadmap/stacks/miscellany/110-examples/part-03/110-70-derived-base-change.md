---
declaration: section
origin: cited
lean: Stacks.Examples.no_derived_base_change
statement: formalized
proof: formalized
---

# 110.70 Derived base change

Section 110.70 of the Stacks Project, [Tag 08J2](https://stacks.math.columbia.edu/tag/08J2). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08J3, a lemma

[Tag 08J3](https://stacks.math.columbia.edu/tag/08J3) in the Stacks Project.

**`Stacks.Examples.no_derived_base_change`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/NoDerivedBaseChange.lean, line 811](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/NoDerivedBaseChange.lean#L811).

> In general, derived base change of `A`-modules to `R'` does not factor
> through the derived category of the ordinary tensor-product algebra.

```lean
public theorem no_derived_base_change :
    ∃ (R : Type u), ∃ (hR : CommRing R),
      letI : CommRing R := hR
      ∃ (A : Type u), ∃ (hA : CommRing A),
        letI : CommRing A := hA
        ∃ (R' : Type u), ∃ (hR' : CommRing R'),
          letI : CommRing R' := hR'
          ∃ (f : R →+* A) (g : R →+* R'),
            letI : Algebra R A := f.toAlgebra
            letI : Algebra R R' := g.toAlgebra
            letI : Algebra R' (A ⊗[R] R') := Algebra.TensorProduct.rightAlgebra
            ¬ ∃ (T : DerivedCategory (ModuleCat.{u} A) ⥤
                DerivedCategory (ModuleCat.{u} (A ⊗[R] R'))),
              ∀ (M : ModuleCat.{u} A),
                Nonempty
                  (((ModuleCat.restrictScalars
                      (algebraMap R' (A ⊗[R] R'))).mapDerivedCategory.obj
                        (T.obj ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj M))) ≅
                    ((derivedExtensionScalarsGeneral.{u, u, u} g).functor.obj
                      ((ModuleCat.restrictScalars f).mapDerivedCategory.obj
                        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj M))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.70, Tag 08J2](https://stacks.math.columbia.edu/tag/08J2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
