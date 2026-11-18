---
catalog: module
lean: Cslib.StatefulProcesses.Network, Cslib.StatefulProcesses.Network.TrLabel, Cslib.StatefulProcesses.Network.Tr, Cslib.StatefulProcesses.Network.lts, Cslib.StatefulProcesses.Cfg, Cslib.StatefulProcesses.Cfg.TrLabel, Cslib.StatefulProcesses.Cfg.Tr, Cslib.StatefulProcesses.Cfg.lts
statement: formalized
proof: formalized
---

# Networks of stateful processes and their semantics

`Cslib.Languages.StatefulProcesses.Network`, in [Cslib/Languages/StatefulProcesses/Network.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Network.lean), by Fabrizio Montesi.

> This module defines networks (maps from process names to process terms), as well as their symbolic
> and concrete operational semantics.
>
> ## Implementation notes
>
> We leverage the fact that networks are functions to formulate the semantics without requiring a
> definition of parallel composition.
>
> ## References
>
> * [F. Montesi, *Introduction to Choreographies*][Montesi2023]

> ## Networks and their symbolic semantics

`Cslib.StatefulProcesses.Network` (abbreviation, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Network.lean#L36))

> A network maps process names to process terms.

```lean
abbrev Network (Pid Var Val FunId SelLabel ProcName : Type*)
```

`Cslib.StatefulProcesses.Network.TrLabel` (inductive type, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Network.lean#L43))

> Symbolic transition labels for networks.

```lean
inductive Network.TrLabel Pid Var Val FunId SelLabel
  | local (p : Pid) (μ : Act Pid Var Val FunId SelLabel)
  | com (p : Pid) (e : Expr Var Val FunId) (q : Pid) (x : Var)
  | sel (p : Pid) (q : Pid) (l : SelLabel)
```

`Cslib.StatefulProcesses.Network.Tr` (inductive type, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Network.lean#L51))

> Symbolic transition relation for networks.

```lean
inductive Network.Tr :
    Network Pid Var Val FunId SelLabel ProcName → TrLabel Pid Var Val FunId SelLabel →
    Network Pid Var Val FunId SelLabel ProcName → Prop
  | local
    (hμ : μ.isInternal) (htr : Process.lts.Tr (n p) μ prP)
    (hn' : n' = n[p := prP]) :
    Tr n (TrLabel.local p μ) n'
  | com
    (hsend : Process.lts.Tr (n p) (.sendValue q e) prP)
    (hrecv : Process.lts.Tr (n q) (.recvValue p x) prQ)
    (hn' : n' = n[p := prP][q := prQ]) :
    Tr n (TrLabel.com p e q x) n'
  | sel
    (hsend : Process.lts.Tr (n p) (.sendLabel q l) prP)
    (hrecv : Process.lts.Tr (n q) (.recvLabel p l) prQ)
    (hn' : n' = n[p := prP][q := prQ]) :
    Tr n (TrLabel.sel p q l) n'
```

`Cslib.StatefulProcesses.Network.lts` (definition, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Network.lean#L70))

> Symbolic LTS of networks.

```lean
def Network.lts :
    LTS (Network Pid Var Val FunId SelLabel ProcName) (TrLabel Pid Var Val FunId SelLabel)
```

> ## Stores, evaluation, and concrete semantics of networks

`Cslib.StatefulProcesses.Cfg` (structure, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Network.lean#L77))

> Configurations, consisting of a network and a global store.

```lean
structure Cfg (Pid Var Val FunId SelLabel ProcName : Type*) where
  /-- The network of the configuration. -/
  net : Network Pid Var Val FunId SelLabel ProcName
  /-- The global store of the configuration. -/
  store : GlobalStore Pid Var Val
```

`Cslib.StatefulProcesses.Cfg.TrLabel` (inductive type, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Network.lean#L88))

> Transition labels for network configurations.
>
> These labels model what can be observed from execution, and thus hide internal computational
> details.

```lean
inductive Cfg.TrLabel Pid Val SelLabel
  | local (p : Pid)
  | com (p : Pid) (q : Pid) (v : Val)
  | sel (p : Pid) (q : Pid) (l : SelLabel)
```

`Cslib.StatefulProcesses.Cfg.Tr` (inductive type, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Network.lean#L94))

> Transition relation for network configurations.

```lean
inductive Cfg.Tr [DecidableEq Var] (isTrue : Val → Bool) (Eval : FunCallEval FunId Val) :
    Cfg Pid Var Val FunId SelLabel ProcName → Cfg.TrLabel Pid Val SelLabel →
    Cfg Pid Var Val FunId SelLabel ProcName → Prop where
  -- Internal actions
  | assign
    (htr : Network.lts.Tr cfg.net (.local p (.assign x e)) cfg'.net)
    (heval : Eval.EvalExpr (cfg.store p) e v)
    (hstore : cfg'.store = cfg.store[(p, x) := v]) :
    Tr isTrue Eval cfg (Cfg.TrLabel.local p) cfg'
  | condThen
    (htr : Network.lts.Tr cfg.net (.local p (.condThen e)) cfg'.net)
    (heval : Eval.EvalExpr (cfg.store p) e v)
    (hguard : isTrue v)
    (hstore : cfg'.store = cfg.store) :
    Tr isTrue Eval cfg (Cfg.TrLabel.local p) cfg'
  | condElse
    (htr : Network.lts.Tr cfg.net (.local p (.condElse e)) cfg'.net)
    (heval : Eval.EvalExpr (cfg.store p) e v)
    (hguard : ¬isTrue v)
    (hstore : cfg'.store = cfg.store) :
    Tr isTrue Eval cfg (Cfg.TrLabel.local p) cfg'
  -- Interactions
  | com
    (htr : Network.lts.Tr cfg.net (.com p e q x) cfg'.net)
    (heval : Eval.EvalExpr (cfg.store p) e v)
    (hstore : cfg'.store = cfg.store[(q, x) := v]) :
    Tr isTrue Eval cfg (Cfg.TrLabel.com p q v) cfg'
  | sel
    (htr : Network.lts.Tr cfg.net (.sel p q l) cfg'.net)
    (hstore : cfg'.store = cfg.store) :
    Tr isTrue Eval cfg (Cfg.TrLabel.sel p q l) cfg'
```

`Cslib.StatefulProcesses.Cfg.lts` (definition, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Network.lean#L127))

> LTS of network configurations.

```lean
def Cfg.lts [DecidableEq Var] (isTrue : Val → Bool) (Eval : FunCallEval FunId Val) :
    LTS (Cfg Pid Var Val FunId SelLabel ProcName) (Cfg.TrLabel Pid Val SelLabel)
```

## Depends on

- [Stateful Processes](basic.md)

## Sources

- [Cslib/Languages/StatefulProcesses/Network.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Network.lean)
