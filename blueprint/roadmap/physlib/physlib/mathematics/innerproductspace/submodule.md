---
declaration: module
origin: cited
lean: InnerProductSpaceSubmodule.submoduleToLp, InnerProductSpaceSubmodule.mem_submodule_iff_mem_submoduleToLp, InnerProductSpaceSubmodule.submoduleToLp_closure, InnerProductSpaceSubmodule.mem_submodule_closure_iff_mem_submoduleToLp_closure, InnerProductSpaceSubmodule.mem_submodule_adjoint_iff_mem_submoduleToLp_orthogonal, InnerProductSpaceSubmodule.mem_submodule_adjoint_adjoint_iff_mem_submoduleToLp_orthogonal_orthogonal, InnerProductSpaceSubmodule.mem_submodule_closure_adjoint_iff_mem_submoduleToLp_closure_orthogonal
statement: formalized
proof: formalized
---

# Submodules of `E × F`

The module `Physlib.Mathematics.InnerProductSpace.Submodule`, [Physlib/Mathematics/InnerProductSpace/Submodule.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Submodule.lean): 7 declarations, 1 with a docstring.

> In this module we define `submoduleToLp` which reinterprets a submodule of `E × F`,
> where `E` and `F` are inner product spaces, as a submodule of `WithLp 2 (E × F)`.
> This allows us to take advantage of the inner product structure, since otherwise
> by default `E × F` is given the sup norm.

**`InnerProductSpaceSubmodule.submoduleToLp`**, a def, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Submodule.lean#L33).

> The submodule of `WithLp 2 (E × F)` defined by `M`.

```lean
def submoduleToLp : Submodule ℂ (WithLp 2 (E × F))
```

**`InnerProductSpaceSubmodule.mem_submodule_iff_mem_submoduleToLp`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Submodule.lean#L43).

```lean
lemma mem_submodule_iff_mem_submoduleToLp : f ∈ M ↔ (WithLp.toLp 2 f) ∈ submoduleToLp M
```

**`InnerProductSpaceSubmodule.submoduleToLp_closure`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Submodule.lean#L46).

```lean
lemma submoduleToLp_closure :
    (submoduleToLp M.topologicalClosure) = (submoduleToLp M).topologicalClosure
```

**`InnerProductSpaceSubmodule.mem_submodule_closure_iff_mem_submoduleToLp_closure`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Submodule.lean#L76).

```lean
lemma mem_submodule_closure_iff_mem_submoduleToLp_closure :
    f ∈ M.topologicalClosure ↔ (WithLp.toLp 2 f) ∈ (submoduleToLp M).topologicalClosure
```

**`InnerProductSpaceSubmodule.mem_submodule_adjoint_iff_mem_submoduleToLp_orthogonal`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Submodule.lean#L81).

```lean
lemma mem_submodule_adjoint_iff_mem_submoduleToLp_orthogonal :
    g ∈ M.adjoint ↔ WithLp.toLp 2 (g.2, -g.1) ∈ (submoduleToLp M)ᗮ
```

**`InnerProductSpaceSubmodule.mem_submodule_adjoint_adjoint_iff_mem_submoduleToLp_orthogonal_orthogonal`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Submodule.lean#L100).

```lean
lemma mem_submodule_adjoint_adjoint_iff_mem_submoduleToLp_orthogonal_orthogonal :
    f ∈ M.adjoint.adjoint ↔ WithLp.toLp 2 f ∈ (submoduleToLp M)ᗮᗮ
```

**`InnerProductSpaceSubmodule.mem_submodule_closure_adjoint_iff_mem_submoduleToLp_closure_orthogonal`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Submodule.lean#L121).

```lean
lemma mem_submodule_closure_adjoint_iff_mem_submoduleToLp_closure_orthogonal :
    g ∈ M.topologicalClosure.adjoint ↔
    WithLp.toLp 2 (g.2, -g.1) ∈ (submoduleToLp M).topologicalClosureᗮ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/InnerProductSpace/Submodule.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Submodule.lean)
