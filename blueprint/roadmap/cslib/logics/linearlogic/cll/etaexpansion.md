---
catalog: module
lean: Cslib.Logic.CLL.Proposition.expand, Cslib.Logic.CLL.Proof.onlyAtomicAxioms, Cslib.Logic.CLL.Proof.onlyAtomicAxioms_rwConclusion, Cslib.Logic.CLL.Proof.expand_onlyAtomicAxioms
statement: formalized
proof: formalized
---

# η-expansion for Classical Linear Logic (CLL)

`Cslib.Logics.LinearLogic.CLL.EtaExpansion`, in [Cslib/Logics/LinearLogic/CLL/EtaExpansion.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/EtaExpansion.lean), by Fabrizio Montesi.

`Cslib.Logic.CLL.Proposition.expand` (definition, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/EtaExpansion.lean#L29))

> The η-expansion of a proposition `a` is a `Proof` of `{a, a⫠}` that applies the axiom
> only to atomic propositions.

```lean
def Proposition.expand (a : Proposition Atom) : ⇓({a, a⫠} : Sequent Atom)
```

`Cslib.Logic.CLL.Proof.onlyAtomicAxioms` (definition, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/EtaExpansion.lean#L81))

> A `Proof` has only atomic axioms if all its instances of the axiom treat atomic propositions.

```lean
def Proof.onlyAtomicAxioms {Γ : Sequent Atom} (p : ⇓Γ) : Bool
```

`Cslib.Logic.CLL.Proof.onlyAtomicAxioms_rwConclusion` (theorem, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/EtaExpansion.lean#L99))

> `Proof.onlyAtomicAxioms` is preserved by `Proof.rwConclusion`.

```lean
theorem Proof.onlyAtomicAxioms_rwConclusion {Γ Δ : Sequent Atom} {heq : Γ = Δ} {p : ⇓Γ}
    (h : p.onlyAtomicAxioms) :
  (rwConclusion heq p).onlyAtomicAxioms
```

`Cslib.Logic.CLL.Proof.expand_onlyAtomicAxioms` (theorem, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/EtaExpansion.lean#L118))

> η-expansion is correct: the proof returned by η-expansion contains only atomic axioms.

```lean
theorem Proof.expand_onlyAtomicAxioms (a : Proposition Atom) : a.expand.onlyAtomicAxioms
```

## Depends on

- [Classical Linear Logic](basic.md)

## Sources

- [Cslib/Logics/LinearLogic/CLL/EtaExpansion.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/EtaExpansion.lean)
