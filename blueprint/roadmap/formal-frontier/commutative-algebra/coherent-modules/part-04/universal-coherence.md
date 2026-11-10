---
declaration: class
origin: cited
lean: IsUniversallyCoherent
statement: formalized
---

# Universal coherence

[`IsUniversallyCoherent`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/UniversallyCoherent.lean)
asserts coherence for finitely presented commutative algebras in an independently
chosen target universe; the library derives base coherence at `v = u` and
supplies the Noetherian case. Finitely presented algebra extensions preserve universal
coherence with independent base, extension and target universes. In particular, polynomial
rings over universally coherent rings are universally coherent; no module-finiteness
hypothesis is needed. Coherence of all finite-variable polynomial rings characterizes
universal coherence at the base-ring universe and implies universal coherence in every
independently chosen target universe. In particular, base-universe universal coherence
suffices for arbitrary target universes; no converse from an arbitrary smaller target
universe is asserted. Polynomial rings in an arbitrary type of variables over a
base-universe universally coherent ring are universally coherent, with independent
variable and target universes; neither finitely many variables nor a Noetherian base is
required. Arbitrary localizations of base-universe universally coherent rings are
universally coherent, with independent localization and target universes. No finite
denominator family or algebra finite-presentation hypothesis on the localization is needed.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `IsUniversallyCoherent` (class), declared in [CoherentModules/UniversallyCoherent.lean, line 87](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/UniversallyCoherent.lean#L87).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `IsUniversallyCoherent` in CoherentModules/UniversallyCoherent.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/UniversallyCoherent.lean#L87)
