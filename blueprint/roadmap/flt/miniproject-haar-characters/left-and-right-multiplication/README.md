# Left and right multiplication

If $R$ is a locally compact topological ring, and if multiplication on $R$ is not commutative, then left and right multiplication by an element of $R$ can scale Haar measure in different ways. For example if $R$ is the upper-triangular $2\times 2$ matrices with real entries, then left multiplication by $\begin{pmatrix}a&0\\0&1\end{pmatrix}$ sends $\begin{pmatrix}x&y\\0&z\end{pmatrix}$ to $\begin{pmatrix}ax&ay\\0&z\end{pmatrix}$ and thus scales $R$'s additive Haar measure by $|a|^2$, but right multiplication by $\begin{pmatrix}a&0\\0&1\end{pmatrix}$ sends $\begin{pmatrix}x&y\\0&z\end{pmatrix}$ to $\begin{pmatrix}ax&y\\0&z\end{pmatrix}$ and thus scales $R$'s additive Haar measure by a factor of $|a|$.

What's going on here is that if we regard left and right multiplication as $\mathbb{R}$-linear maps from $R$ to $R$, then their associated matrices with respect to the obvious basis are $diag(a,a,1)$ and $diag(a,1,1)$, which have different determinants.

However, if $k$ is now any field and if $B$ is a finite-dimensional central simple algebra over $k$ (for example a quaternion algebra, the case we'll care about later), and if $u\in B^\times$ then $x\mapsto ux$ and $x\mapsto xu$ are both $k$-linear endomorphisms of $B$, and I claim that they have the same determinant.

- [IsSimpleRing.mulLeft\_det\_eq\_mulRight\_det](issimplering-mulleft-det-eq-mulright-det.md)
- [IsSimpleRing.ringHaarChar\_eq\_addEquivAddHaarChar\_mulRight](issimplering-ringhaarchar-eq-addequivaddhaarchar.md)
