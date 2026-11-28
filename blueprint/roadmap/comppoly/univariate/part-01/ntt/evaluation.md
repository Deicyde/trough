---
catalog: module
lean: CompPoly.CPolynomial.NTT.evalOnDomain, CompPoly.CPolynomial.NTT.evalOnDomain_eq_evalBatch, CompPoly.CPolynomial.NTT.Forward.forwardSpec_eval_node_eq, CompPoly.CPolynomial.NTT.Forward.forwardSpec_eq_evalOnDomain, CompPoly.CPolynomial.NTT.Forward.forwardImpl_eval_node_eq, CompPoly.CPolynomial.NTT.Forward.forwardImpl_eq_evalOnDomain
statement: formalized
proof: formalized
---

# NTT and Evaluation

`CompPoly.Univariate.NTT.Evaluation`, in [CompPoly/Univariate/NTT/Evaluation.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Evaluation.lean), by Valerii Huhnin.

> Bridge definitions and theorems connecting the NTT specification layer to
> evaluation on the root-of-unity domain.

`CompPoly.CPolynomial.NTT.evalOnDomain` (definition, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Evaluation.lean#L29))

> Evaluate a raw polynomial on all nodes of an NTT domain in natural order.

```lean
def evalOnDomain (D : Domain R) (p : CPolynomial.Raw R) : Array R
```

`CompPoly.CPolynomial.NTT.evalOnDomain_eq_evalBatch` (theorem, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Evaluation.lean#L33))

> `evalOnDomain` is `evalBatch` specialized to the NTT domain nodes.

```lean
theorem evalOnDomain_eq_evalBatch (D : Domain R) (p : CPolynomial R) :
    evalOnDomain D p.val =
      evalBatch p (Array.ofFn (fun k : D.Idx => D.node k))
```

`CompPoly.CPolynomial.NTT.Forward.forwardSpec_eval_node_eq` (theorem, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Evaluation.lean#L46))

> Pointwise form: the forward NTT specification evaluates a raw polynomial at a domain node.

```lean
theorem forwardSpec_eval_node_eq (D : Domain R) (p : CPolynomial.Raw R)
    (hdeg : p.toPoly.natDegree < D.n) (k : D.Idx) :
    (forwardSpec D p)[k.1] = p.eval (D.node k)
```

`CompPoly.CPolynomial.NTT.Forward.forwardSpec_eq_evalOnDomain` (theorem, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Evaluation.lean#L68))

> The forward NTT specification evaluates a raw polynomial on all domain nodes.

```lean
theorem forwardSpec_eq_evalOnDomain (D : Domain R) (p : CPolynomial.Raw R)
    (hdeg : p.toPoly.natDegree < D.n) :
    forwardSpec D p = evalOnDomain D p
```

`CompPoly.CPolynomial.NTT.Forward.forwardImpl_eval_node_eq` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Evaluation.lean#L78))

> Pointwise form: the forward NTT implementation evaluates a raw polynomial at a domain node.

```lean
theorem forwardImpl_eval_node_eq (D : Domain R) (p : CPolynomial.Raw R)
    (hdeg : p.toPoly.natDegree < D.n) (k : D.Idx) :
    (forwardImpl D p).getD k.1 0 = p.eval (D.node k)
```

`CompPoly.CPolynomial.NTT.Forward.forwardImpl_eq_evalOnDomain` (theorem, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Evaluation.lean#L86))

> The forward NTT implementation evaluates a raw polynomial on all domain nodes.

```lean
theorem forwardImpl_eq_evalOnDomain (D : Domain R) (p : CPolynomial.Raw R)
    (hdeg : p.toPoly.natDegree < D.n) :
    forwardImpl D p = evalOnDomain D p
```

## Depends on

- [Naive Batch Evaluation](../batcheval/naive.md)
- [Forward NTT](forward.md)
- [Computable Univariate To `Polynomial`](../../part-02/topoly/core.md)

## Sources

- [CompPoly/Univariate/NTT/Evaluation.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Evaluation.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTT.Evaluation.json)
