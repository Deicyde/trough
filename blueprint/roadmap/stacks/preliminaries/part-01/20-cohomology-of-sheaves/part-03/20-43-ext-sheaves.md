---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.derivedSheafExt, Stacks.SheafOfModules.derivedSheafExtFunctor, Stacks.SheafOfModules.derivedSheafExtIsoSheafifyPresheaf, Stacks.SheafOfModules.hypercohomologySpectralSequence_e₂_derivedSheafExt
statement: formalized
proof: formalized
---

# 20.43 Ext sheaves

Section 20.43 of the Stacks Project, [Tag 0BQP](https://stacks.math.columbia.edu/tag/0BQP). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BQP, the section

[Tag 0BQP](https://stacks.math.columbia.edu/tag/0BQP) in the Stacks Project.

**`Stacks.SheafOfModules.derivedSheafExt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/ExtSheaves.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/ExtSheaves.lean#L127). The attribute's comment: “the definition of the Ext sheaves: SheafExt^n(K, L) is the n-th cohomology sheaf of RSheafHom(K, L), for K and L objects of D(O\_X) and n an integer”. References: EGA 0 (12.3.1), “more general”; SGA 4 V (6.0), “special case”.

> **The Ext sheaves.** For objects `K`, `L` of `D(O_X)` and an integer `n`, the Ext sheaf
> `SheafExt^n(K, L)` is the degree-`n` cohomology sheaf of the derived internal Hom
> `RSheafHom(K, L)`, an `O_X`-module.

```lean
abbrev derivedSheafExt (K L : DerivedCategory (StructureSheafModules Rc)) (n : ℤ) :
    StructureSheafModules Rc
```

**`Stacks.SheafOfModules.derivedSheafExtFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/ExtSheaves.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/ExtSheaves.lean#L137). The attribute's comment: “the Ext sheaves are functorial in both variables, contravariantly in the first”. References: EGA 0 (12.3.1), “more general”; SGA 4 V (6.0), “6.0.1, special case”.

> **The Ext sheaves as a bifunctor.** `SheafExt^n(-, -)` is a functor of both variables,
> contravariant in the first: it is the derived internal Hom followed by the degree-`n` cohomology
> sheaf.

```lean
def derivedSheafExtFunctor (n : ℤ) :
    (DerivedCategory (StructureSheafModules Rc))ᵒᵖ ⥤
      DerivedCategory (StructureSheafModules Rc) ⥤ StructureSheafModules Rc
```

**`Stacks.SheafOfModules.derivedSheafExtIsoSheafifyPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/ExtSheaves.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/ExtSheaves.lean#L181). The attribute's comment: “the Ext sheaf is the sheafification of the presheaf of degree-n hypercohomology of RSheafHom(K, L) on the opens of X; the identification of that presheaf's values with the Ext groups Ext^n(K|\_U, L|\_U) is Tag 08DK and is cited, not composed in here”.

> **The Ext sheaf is a sheafification.** `SheafExt^n(K, L)` is the sheaf of `O_X`-modules
> associated to the presheaf of degree-`n` hypercohomology of `RSheafHom(K, L)`, whose value over
> an open `U` is `Ext^n_{D(O_U)}(K|_U, L|_U)` by [Stacks, Tag 08DK].
>
> This is [Stacks, Tag 0BKJ] — a cohomology sheaf is the sheafification of the cohomology presheaf
> — read at `RSheafHom(K, L)`.

```lean
def derivedSheafExtIsoSheafifyPresheaf (K L : DerivedCategory (StructureSheafModules Rc))
    (n : ℤ) :
    (PresheafOfModules.sheafification (𝟙 (structureSheaf Rc).obj)).obj
        (derivedSheafExtPresheaf Rc K L n) ≅ derivedSheafExt Rc K L n
```

**`Stacks.SheafOfModules.hypercohomologySpectralSequence_e₂_derivedSheafExt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/ExtSheaves.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/ExtSheaves.lean#L222). The attribute's comment: “the second page of the local-to-global spectral sequence of Ext: the Tag 0BKM hypercohomology spectral sequence of RSheafHom(K, L) has E\_2^\{p, q} = H^p(X, SheafExt^q(K, L)); convergence to Ext^\{p+q}(K, L) is not claimed here -- the Tag 0BKM convergence clause needs a bounded below complex representing RSheafHom(K, L) and is stated of an existentially produced spectral sequence rather than of the canonical one carrying this second page, and the Ext reading of the abutment is Tag 08DK”. References: SGA 7 VIII (1.1), “partial”.

> **The second page of the local-to-global spectral sequence of Ext.** The hypercohomology
> spectral sequence of [Stacks, Tag 0BKM] applied to `RSheafHom(K, L)` has second page
>
> `E_2^{p, q} = H^p(X, SheafExt^q(K, L))`,
>
> the hypercohomology of the Ext sheaves. Its abutment is `H^{p + q}(X, RSheafHom(K, L))`, which is
> `Ext^{p + q}_{D(O_X)}(K, L)` by [Stacks, Tag 08DK].

```lean
theorem hypercohomologySpectralSequence_e₂_derivedSheafExt
    (K L : DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing Y))) (p q : ℤ) :
    Nonempty ((((hypercohomologySpectralSequence Y
          (((derivedSheafHom Y.sheaf).obj (op K)).obj L)).spectralSequence.page 2).X (p, q)) ≅
      (DerivedCategory.homologyFunctor
          (ModuleCat.{u} ((structureSheafRing Y).obj.obj (op ⊤))) p).obj
        ((hypercohomologySpectralSequence Y
            (((derivedSheafHom Y.sheaf).obj (op K)).obj L)).truncation.RΓ.obj
          ((DerivedCategory.singleFunctor (_root_.SheafOfModules.{u} (structureSheafRing Y)) 0).obj
            (derivedSheafExt Y.sheaf K L q))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.43, Tag 0BQP](https://stacks.math.columbia.edu/tag/0BQP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
