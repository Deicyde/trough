---
declaration: theorem
origin: cited
lean: TauCeti.IsVertexStrong.isArcStrong, TauCeti.vertexStrongConnectivity_le_arcConnectivity
statement: formalized
proof: formalized
---

# The directed Whitney inequality

A `k`-vertex-strong arrow family is `k`-arc-strong.

```lean
TauCeti.IsVertexStrong.isArcStrong.{u, v} {V : Type u} {Q : V → V → Type v} {k : ℕ}
  (h : TauCeti.IsVertexStrong Q k) : TauCeti.IsArcStrong Q k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsVertexStrong.isArcStrong`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Connectivity/Basic.html#TauCeti.IsVertexStrong.isArcStrong).

## Other forms

**The directed Whitney inequality, numerical form.** Formalized in Tau Ceti as [`TauCeti.vertexStrongConnectivity_le_arcConnectivity`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Connectivity/Basic.html#TauCeti.vertexStrongConnectivity_le_arcConnectivity).

```lean
TauCeti.vertexStrongConnectivity_le_arcConnectivity.{u, v} {V : Type u} {Q : V → V → Type v} :
  TauCeti.vertexStrongConnectivity Q ≤ TauCeti.arcConnectivity Q
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsVertexStrong.isArcStrong`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Connectivity/Basic.html#TauCeti.IsVertexStrong.isArcStrong)
- [Source of `TauCeti.IsVertexStrong.isArcStrong` in TauCeti/Combinatorics/Network/Connectivity/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Network/Connectivity/Basic.lean#L251)
