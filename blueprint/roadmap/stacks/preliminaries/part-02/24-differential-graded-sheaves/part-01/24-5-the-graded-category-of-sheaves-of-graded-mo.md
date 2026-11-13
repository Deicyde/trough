---
declaration: section
origin: cited
lean: SheafOfModules.GradedHomOfDegree, SheafOfModules.GradedHomOfDegree.comp, SheafOfModules.GradedHomOfDegree.id, SheafOfModules.GradedHomOfDegree.add_comp, SheafOfModules.GradedHomOfDegree.comp_add, SheafOfModules.GradedHomOfDegree.smul_comp, SheafOfModules.GradedHomOfDegree.comp_smul, SheafOfModules.GradedHomOfDegree.components
statement: formalized
proof: formalized
---

# 24.5 The graded category of sheaves of graded modules

Section 24.5 of the Stacks Project, [Tag 0FR1](https://stacks.math.columbia.edu/tag/0FR1). 1 tag here is carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FR1, the section

[Tag 0FR1](https://stacks.math.columbia.edu/tag/0FR1) in the Stacks Project.

**`SheafOfModules.GradedHomOfDegree`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHom.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHom.lean#L300). The attribute's comment: “homogeneous homomorphisms of degree n of right graded modules”.

> A homomorphism of right graded `A`-modules homogeneous of degree `n`: a family of morphisms
> `M^i ⟶ L^{i + n}` of sheaves of modules compatible with the right action. These are the
> elements of `Hom^n` in the graded category of right graded `A`-modules.

```lean
structure GradedHomOfDegree (M L : GradedModule.{t, a, w} A) (n : ℤ)
```

**`SheafOfModules.GradedHomOfDegree.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean, line 765](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean#L765). The attribute's comment: “composition `Hom^m(L, M) × Hom^n(K, L) → Hom^{n + m}(K, M)` in `Mod^gr(A)`”.

> **Composition in the graded category `Mod^gr(A)` of Stacks 0FR1**: the composite
> `g ∘ f : K → M`, homogeneous of degree `n + m`, of homogeneous homomorphisms `f : K → L` of
> degree `n` and `g : L → M` of degree `m`.

```lean
def comp (g : GradedHomOfDegree L M m) (f : GradedHomOfDegree K L n) :
    GradedHomOfDegree K M (n + m)
```

**`SheafOfModules.GradedHomOfDegree.id`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean#L94). The attribute's comment: “the identity of `Mod^gr(A)`, in `Hom^0(M, M)`”.

> **The identity in `Mod^gr(A)`**: the identity of a right graded `A`-module, homogeneous of
> degree zero.

```lean
def id (M : GradedModule.{t, a, w} A) : GradedHomOfDegree M M 0
```

**`SheafOfModules.GradedHomOfDegree.add_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean#L148). The attribute's comment: “composition is additive in `g`”.

> Composition in `Mod^gr(A)` is additive in the first variable.

```lean
theorem add_comp (g g' : GradedHomOfDegree L M m) (f : GradedHomOfDegree K L n) :
    (g + g').comp f = g.comp f + g'.comp f
```

**`SheafOfModules.GradedHomOfDegree.comp_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean#L157). The attribute's comment: “composition is additive in `f`”.

> Composition in `Mod^gr(A)` is additive in the second variable.

```lean
theorem comp_add (g : GradedHomOfDegree L M m) (f f' : GradedHomOfDegree K L n) :
    g.comp (f + f') = g.comp f + g.comp f'
```

**`SheafOfModules.GradedHomOfDegree.smul_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean#L165). The attribute's comment: “composition is `R`-linear in `g`”.

> Composition in `Mod^gr(A)` is `Γ(C, O)`-linear in the first variable.

```lean
theorem smul_comp (c : Stacks.Cohomology.SiteModules.GlobalSectionRing R)
    (g : GradedHomOfDegree L M m) (f : GradedHomOfDegree K L n) :
    (c • g).comp f = c • g.comp f
```

**`SheafOfModules.GradedHomOfDegree.comp_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean#L173). The attribute's comment: “composition is `R`-linear in `f`”.

> Composition in `Mod^gr(A)` is `Γ(C, O)`-linear in the second variable.

```lean
theorem comp_smul (c : Stacks.Cohomology.SiteModules.GlobalSectionRing R)
    (g : GradedHomOfDegree L M m) (f : GradedHomOfDegree K L n) :
    g.comp (c • f) = c • g.comp f
```

**`SheafOfModules.GradedHomOfDegree.components`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean#L210). The attribute's comment: “the components `f_{p, q} : L^{-q} → M^p`, `p + q = n`, of `f ∈ Hom^n(L, M)`”.

> **The components of a homogeneous map** (Stacks 0FR1): a map `f` homogeneous of degree `n`
> as the family `f_{p, q} : L^{-q} → M^p`, `p + q = n`, of its components; the reversal of indices
> is that of the source.

```lean
def components (f : GradedHomOfDegree L M n) (p q : ℤ) (h : p + q = n) :
    L.piece (-q) ⟶ M.piece p
```

**`SheafOfModules.GradedHomOfDegree.componentsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean#L291). The attribute's comment: “`Hom^n(L, M) ⊂ ∏_{p + q = n} Hom_O(L^{-q}, M^p)` is the subset of the families with `f_{p, q}(m a) = f_{p - i, q + i}(m) a`”.

> **Stacks 0FR1, in terms of components**: `Hom^n(L, M)` is the subset of
> `∏_{p + q = n} Hom_O(L^{-q}, M^p)` of the families `f = (f_{p, q})` with
> `f_{p, q}(m a) = f_{p - i, q + i}(m) a`; a homogeneous map corresponds to the family of its
> components.

```lean
def componentsEquiv (L M : GradedModule.{t, a, w} A) (n : ℤ) :
    GradedHomOfDegree L M n ≃
      {f : ∀ p q : ℤ, p + q = n → (L.piece (-q) ⟶ M.piece p) // IsComponentFamily f}
```

**`SheafOfModules.GradedModuleCat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean#L369). The attribute's comment: “the objects of `Mod^gr(A)`: right graded `A`-modules”.

> **The graded category `Mod^gr(A)` of Stacks 0FR1**: its objects are the right graded
> `A`-modules. This is a type synonym so that it can carry the category structure whose morphisms
> are the finite sums of homogeneous maps, rather than only the maps of degree zero.

```lean
def GradedModuleCat (A : GradedAlgebra.{t, a} R)
```

**`SheafOfModules.GradedModuleCat.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean#L463). The attribute's comment: “`Hom_{Mod^gr(A)}(L, M) = ⨁_n Hom^n(L, M)`, with composition `(g, f) ↦ g ∘ f`”.

> **The category `Mod^gr(A)` of Stacks 0FR1**: the morphisms `L → M` are
> `⨁_n Hom^n(L, M)`, and composition is composition of homogeneous maps,
> `Hom^m(L, M) × Hom^n(K, L) → Hom^{n + m}(K, M)`, extended additively.

```lean
noncomputable instance instCategory : Category (GradedModuleCat.{t, a, w} A)
```

**`SheafOfModules.GradedModuleCat.instLinear`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean, line 517](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean#L517). The attribute's comment: “`Mod^gr(A)` is `R`-linear, `R = Γ(C, O)`”.

> `Mod^gr(A)` is linear over `R = Γ(C, O)`: composition is `R`-bilinear.

```lean
noncomputable instance instLinear :
    Linear (Stacks.Cohomology.SiteModules.GlobalSectionRing R) (GradedModuleCat.{t, a, w} A)
```

**`SheafOfModules.GradedModuleCat.instGradedCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean, line 529](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean#L529). The attribute's comment: “`Mod^gr(A)` is a graded category over `R = Γ(C, O)` with degree-`n` morphisms `Hom^n(L, M)`”.

> **The graded category `Mod^gr(A)` over `R = Γ(C, O)` of Stacks 0FR1**: the degree-`n`
> morphisms `L → M` are the homogeneous maps `Hom^n(L, M)`, identities have degree zero and
> composition adds degrees.

```lean
noncomputable instance instGradedCategory :
    GradedCategory (Stacks.Cohomology.SiteModules.GlobalSectionRing R)
      (GradedModuleCat.{t, a, w} A)
```

**`SheafOfModules.GradedModuleCat.degreeZeroEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean, line 625](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleGradedCategory.lean#L625). The attribute's comment: “the associated category `(Mod^gr(A))^0` is the category of graded `A`-modules”.

> **The associated category of `Mod^gr(A)` (Stacks 0FR1)**: the degree-zero category
> `(Mod^gr(A))^0` is equivalent to the category of graded `A`-modules, by the identity on objects;
> a degree-zero morphism is its degree-zero part, a homomorphism of graded `A`-modules.

```lean
noncomputable def degreeZeroEquivalence :
    DegreeZero (Stacks.Cohomology.SiteModules.GlobalSectionRing R) (GradedModuleCat.{t, a, w} A) ≌
      GradedModule.{t, a, w} A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.5, Tag 0FR1](https://stacks.math.columbia.edu/tag/0FR1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
