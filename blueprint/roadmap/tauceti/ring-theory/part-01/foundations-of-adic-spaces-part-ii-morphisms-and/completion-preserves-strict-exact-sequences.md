---
declaration: theorem
origin: cited
lean: AddMonoidHom.exact_completion
statement: formalized
proof: formalized
---

# Completion preserves strict exact sequences

If `M → N → P` is exact with strict maps,
where `M` is a first-countable nonarchimedean group and `N` is a nonarchimedean group, then the
sequence of separated completions is exact. Its maps are again strict by
`AddMonoidHom.isStrictMap_completion` when `M` and `N` are first countable. No Hausdorff
hypothesis is needed.

```lean
AddMonoidHom.exact_completion.{u_3, u_4, u_5} {M : Type u_3} {N : Type u_4} {P : Type u_5}
  [AddCommGroup M] [UniformSpace M] [IsUniformAddGroup M] [NonarchimedeanAddGroup M]
  [(nhds 0).IsCountablyGenerated] [AddCommGroup N] [UniformSpace N] [IsUniformAddGroup N]
  [NonarchimedeanAddGroup N] [AddGroup P] [UniformSpace P] [IsUniformAddGroup P] {f : M →+ N}
  {g : N →+ P} (hf : Topology.IsStrictMap ⇑f) (hg : Topology.IsStrictMap ⇑g)
  (hfg : Function.Exact ⇑f ⇑g) : Function.Exact ⇑(f.completion ⋯) ⇑(g.completion ⋯)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AddMonoidHom.exact_completion`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Nonarchimedean/Completion/Strict.html#AddMonoidHom.exact_completion).

## Sources

- [Tau Ceti documentation: `AddMonoidHom.exact_completion`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Nonarchimedean/Completion/Strict.html#AddMonoidHom.exact_completion)
- [Source of `AddMonoidHom.exact_completion` in TauCeti/Topology/Algebra/Nonarchimedean/Completion/Strict.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Nonarchimedean/Completion/Strict.lean#L102)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
