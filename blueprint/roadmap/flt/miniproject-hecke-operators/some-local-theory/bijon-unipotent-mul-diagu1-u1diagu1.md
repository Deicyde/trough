---
declaration: lemma
origin: cited
lean: TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm.HeckeOperator.Local.bijOn_unipotentMulDiagU1
statement: formalized
proof: formalized
---

# bijOn\_unipotent\_mul\_diagU1\_U1diagU1

The double coset space $UgU$ is the disjoint union of $g_tU$ as $t$ ranges through $\mathcal{O}_v/\alpha\mathcal{O}_v$ and $g_t:=\begin{pmatrix}\alpha&\tilde{t}\\0&1\end{pmatrix}$, where $\tilde{t}$ is any lift of $t$ to $\mathcal{O}_v$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We first manipulate the statement into a statement about finite groups. We have $UgU=\coprod_t g_tU\iff UgUg^{-1}=\coprod_t g_tUg^{-1}=\coprod_t g_tg^{-1}(gUg^{-1})$. By the second isomorphism theorem this is true if $U=\coprod_t g_tg^{-1}(gUg^{-1}\cap U)$. So when is an element of $U$ in $gUg^{-1}$? Equivalently, if $x\in U$, when is $g^{-1}xg\in U$? An explicit calculation of matrices shows us that this is true iff $g=\begin{pmatrix} a&b\\c&d\end{pmatrix}$ with $\alpha\mid b$. Define $U^\alpha$ to be this subgroup of $U$. We have reduced the question to showing that the matrices $h_t:=\begin{pmatrix}1&\tilde{t}\\0&1\end{pmatrix}$ are a set of left coset representatives for the subgroup $U^\alpha$ of $U$.

It thus suffices to show that if $u=\begin{pmatrix} a&b\\c&d\end{pmatrix}\in U$ then $u\in h_tU^\alpha$ iff $b\in\mathcal{O}_v$ reduces mod $\alpha$ to $t\in\mathcal{O}_v/\alpha$. We do this by computing $h_t^{-1}u=\begin{pmatrix} a-\tilde{t}c&b-\tilde{t}d\\c&d\end{pmatrix}$ and observing that its top right hand entry mod $\alpha$ is zero iff $b$ mod $\alpha$ is $t$.

## Lean

Formalized as [`TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm.HeckeOperator.Local.bijOn_unipotentMulDiagU1`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm.HeckeOperator.Local.bijOn_unipotentMulDiagU1).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 436](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HeckeOperatorProject.tex#L436)
