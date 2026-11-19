# First order differential relations

- [rel](def-rel.md)
- [formal_sol](def-formal-sol.md)
- [htpy_formal_sol](def-htpy-formal-sol.md)

The next definition will be used in cases where $X$ and $Y$ are vector spaces, in order to relate the global theory to the local one.

- [transfer_map](def-transfer-map.md)

The following is a localization lemma needed to take advantage of all the work from the previous chapter.

- [transfer](lem-transfer.md)
- [h-princ](def-h-princ.md)

## Parametricity for free

In many cases, relative parametric $h$-principles can be deduced from relative non-parametric ones with a larger source manifold. Let $X$, $P$ and $Y$ be manifolds, with $P$ seen a parameter space. Denote by $Ψ$ the map from $J^1(X × P, Y)$ to $J^1(X, Y)$ sending $(x, p, y, ψ)$ to $(x, y, ψ ∘ ι_{x, p})$ where $ι_{x, p} : T_xX → T_xX × T_pP$ sends $v$ to $(v, 0)$.

To any family of sections $F_p : x ↦ (f_p(x), φ_{p, x})$ of $J^1(X, Y)$, we associate the section $\bar F$ of $J^1(X × P, Y)$ sending $(x, p)$ to $\bar F(x, p) := (f_p(x), φ_{p, x} ⊕ ∂f/∂p(x, p))$.

- [param_trick](lem-param-trick.md)
- [param_for_free](lem-param-for-free.md)
