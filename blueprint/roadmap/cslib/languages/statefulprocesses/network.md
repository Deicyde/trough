---
catalog: module
lean: Cslib.StatefulProcesses.Network, Cslib.StatefulProcesses.Network.TrLabel, Cslib.StatefulProcesses.Network.Tr, Cslib.StatefulProcesses.Network.lts, Cslib.StatefulProcesses.Cfg, Cslib.StatefulProcesses.Cfg.TrLabel, Cslib.StatefulProcesses.Cfg.Tr, Cslib.StatefulProcesses.Cfg.lts
statement: formalized
proof: formalized
---

# Networks of stateful processes and their semantics

`Cslib.Languages.StatefulProcesses.Network`, in [Cslib/Languages/StatefulProcesses/Network.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Network.lean), by Fabrizio Montesi.

> This module defines networks (maps from process names to process terms), as well as their symbolic
> and concrete operational semantics.
>
> ## Implementation notes
>
> We leverage the fact that networks are functions to formulate the semantics without requiring a
> definition of parallel composition.
>
> Networks are parametrised over a signature `S : Sig Pid`, which maps process names to local
> signatures. Each process with name `p` runs a program (`Process`) over its own local signature
> `S p`.
>
> ## References
>
> * [F. Montesi, *Introduction to Choreographies*][Montesi2023]

> ## Networks and their symbolic semantics

`Cslib.StatefulProcesses.Network` (abbreviation, [line 42](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Network.lean#L42))

> A network maps each participant to a process over its local signature.

```lean
abbrev Network (Pid : Type u) (S : Sig.{u, v, w} Pid) (SelLabel ProcName : Type*)
```

`Cslib.StatefulProcesses.Network.TrLabel` (inductive type, [line 48](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Network.lean#L48))

> Symbolic transition labels for networks.

```lean
inductive Network.TrLabel (Pid : Type u) (S : Sig.{u, v, w} Pid) (SelLabel : Type*)
  | local (p : Pid) (μ : Act Pid (S p) SelLabel)
  | com {α : Type w} (p : Pid) (e : S.Expr p α) (q : Pid) (x : S.Var q α)
  | sel (p q : Pid) (l : SelLabel)
```

`Cslib.StatefulProcesses.Network.Tr` (inductive type, [line 56](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Network.lean#L56))

> Symbolic transition relation. Communication connects matching value types.

```lean
inductive Network.Tr : Network Pid S SelLabel ProcName → TrLabel Pid S SelLabel →
    Network Pid S SelLabel ProcName → Prop
  | local {n n' : Network Pid S SelLabel ProcName} {p : Pid} {μ : Act Pid (S p) SelLabel}
      {prP : Process Pid (S p) SelLabel ProcName}
      (hμ : μ.isInternal) (htr : Process.lts.Tr (n p) μ prP)
      (hn' : n' = Function.update n p prP) : Tr n (.local p μ) n'
  | com {n n' : Network Pid S SelLabel ProcName} {p q : Pid} {α : Type w} {e : S.Expr p α}
      {x : S.Var q α} {prP : Process Pid (S p) SelLabel ProcName}
      {prQ : Process Pid (S q) SelLabel ProcName}
      (hsend : Process.lts.Tr (n p) (.sendValue q e) prP)
      (hrecv : Process.lts.Tr (n q) (.recvValue p x) prQ)
      (hn' : n' = Function.update (Function.update n p prP) q prQ) :
      Tr n (.com p e q x) n'
  | sel {n n' : Network Pid S SelLabel ProcName} {p q : Pid} {l : SelLabel}
      {prP : Process Pid (S p) SelLabel ProcName} {prQ : Process Pid (S q) SelLabel ProcName}
      (hsend : Process.lts.Tr (n p) (.sendLabel q l) prP)
      (hrecv : Process.lts.Tr (n q) (.recvLabel p l) prQ)
      (hn' : n' = Function.update (Function.update n p prP) q prQ) :
      Tr n (.sel p q l) n'
```

`Cslib.StatefulProcesses.Network.lts` (definition, [line 77](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Network.lean#L77))

> Symbolic LTS of networks.

```lean
def Network.lts : LTS (Network Pid S SelLabel ProcName) (Network.TrLabel Pid S SelLabel)
```

`Cslib.StatefulProcesses.Cfg` (structure, [line 81](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Network.lean#L81))

> Configurations consist of a network and a local store for every participant.

```lean
structure Cfg (Pid : Type u) (S : Sig.{u, v, w} Pid) (SelLabel ProcName : Type*) where
  /-- Network. -/
  net : Network Pid S SelLabel ProcName
  /-- The global store, with a local store for every participant. -/
  store : S.Store
```

`Cslib.StatefulProcesses.Cfg.TrLabel` (inductive type, [line 88](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Network.lean#L88))

> Observable labels, including the type and value of each communicated message.

```lean
inductive Cfg.TrLabel (Pid SelLabel : Type*)
  | local (p : Pid)
  | com {α : Type w} (p q : Pid) (v : α)
  | sel (p q : Pid) (l : SelLabel)
```

`Cslib.StatefulProcesses.Cfg.Tr` (inductive type, [line 94](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Network.lean#L94))

> Concrete transitions evaluate local expressions in the acting participant's store.

```lean
inductive Cfg.Tr :
    Cfg Pid S SelLabel ProcName → Cfg.TrLabel Pid SelLabel →
    Cfg Pid S SelLabel ProcName → Prop where
  | assign {cfg cfg' : Cfg Pid S SelLabel ProcName} {p : Pid} {α} {x : S.Var p α}
      {e : S.Expr p α} {v : α}
      (htr : Network.lts.Tr cfg.net (.local p (.assign x e)) cfg'.net)
      (heval : e.Eval (cfg.store p) v)
      (hstore : cfg'.store = cfg.store[⟨p, x⟩ := v]) :
      Tr cfg (.local p) cfg'
  | condThen {cfg cfg' : Cfg Pid S SelLabel ProcName} {p : Pid} {α} {_ : HasTrue α}
      {e : S.Expr p α}
      (htr : Network.lts.Tr cfg.net (.local p (.condThen e)) cfg'.net)
      (heval : e.Eval (cfg.store p) HasTrue.true)
      (hstore : cfg'.store = cfg.store) :
      Tr cfg (.local p) cfg'
  | condElse {cfg cfg' : Cfg Pid S SelLabel ProcName} {p : Pid} {α} {_ : HasTrue α}
      {e : S.Expr p α} {v : α}
      (htr : Network.lts.Tr cfg.net (.local p (.condElse e)) cfg'.net)
      (heval : e.Eval (cfg.store p) v) (hne : v ≠ HasTrue.true)
      (hstore : cfg'.store = cfg.store) :
      Tr cfg (.local p) cfg'
  | com {cfg cfg' : Cfg Pid S SelLabel ProcName} {p q : Pid} {α} {e : S.Expr p α}
      {x : S.Var q α} {v : α}
      (htr : Network.lts.Tr cfg.net (.com p e q x) cfg'.net)
      (heval : e.Eval (cfg.store p) v)
      (hstore : cfg'.store = cfg.store[⟨q, x⟩ := v]) :
      Tr cfg (.com p q v) cfg'
  | sel {cfg cfg' : Cfg Pid S SelLabel ProcName} {p q : Pid} {l : SelLabel}
      (htr : Network.lts.Tr cfg.net (.sel p q l) cfg'.net)
      (hstore : cfg'.store = cfg.store) : Tr cfg (.sel p q l) cfg'
```

`Cslib.StatefulProcesses.Cfg.lts` (definition, [line 126](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Network.lean#L126))

> Concrete LTS of configurations.

```lean
def Cfg.lts : LTS (Cfg Pid S SelLabel ProcName) (Cfg.TrLabel.{w} Pid SelLabel)
```

## Depends on

- [Global stores](../mech/common/globalstore.md)
- [Stateful Processes](basic.md)

## Sources

- [Cslib/Languages/StatefulProcesses/Network.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Network.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Languages.StatefulProcesses.Network.json)
