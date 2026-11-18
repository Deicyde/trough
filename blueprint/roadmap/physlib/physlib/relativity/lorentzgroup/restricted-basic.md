---
declaration: module
origin: cited
lean: LorentzGroup.restricted, LorentzGroup.isOrthochronous_of_restricted, LorentzGroup.restricted_normal_subgroup, LorentzGroup.restricted_eq_identity_component_of_isConnected
statement: formalized
proof: formalized
---

# The Restricted Lorentz Group

The module `Physlib.Relativity.LorentzGroup.Restricted.Basic`, [Physlib/Relativity/LorentzGroup/Restricted/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/Basic.lean): 4 declarations, 3 with a docstring.

> This file is currently a stub.

**`LorentzGroup.restricted`**, a def, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/Basic.lean#L26).

> The restricted Lorentz group comprises the proper and orthochronous elements of the
> Lorentz group.

```lean
def restricted (d : ℕ) : Subgroup (LorentzGroup d)
```

**`LorentzGroup.isOrthochronous_of_restricted`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/Basic.lean#L47).

```lean
lemma isOrthochronous_of_restricted {d : ℕ} (Λ : restricted d) :
    IsOrthochronous Λ.1
```

**`LorentzGroup.restricted_normal_subgroup`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/Basic.lean#L51).

> The restricted Lorentz group is a normal subgroup of the Lorentz group.

```lean
lemma restricted_normal_subgroup {d : ℕ} : (restricted d).Normal
```

**`LorentzGroup.restricted_eq_identity_component_of_isConnected`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/Basic.lean#L68).

> Given the hypothesis that the restricted Lorentz group is connected,
> the proof that the restricted lorentz group is equal to the connected component of the
> identity.

```lean
lemma restricted_eq_identity_component_of_isConnected {d : ℕ}
    (h1 : IsConnected (restricted d : Set (LorentzGroup d))) :
    (restricted d) = connectedComponent (1 : LorentzGroup d)
```

## Depends on

- [The Orthochronous Lorentz Group](orthochronous-basic.md)

## Sources

- [Physlib/Relativity/LorentzGroup/Restricted/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/Basic.lean)
