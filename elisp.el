(defvar temp-dir "temp/")
(defvar solved-dir "prob_%s/")
(defvar prob-file "prob_%s.%s")

(defun check-problem (id ext)
  (interactive)
  (setq ext (downcase ext))
  (cond
   ((file-exists-p (solved-problem id ext))
    (format "[[file:%s][X]]" (solved-problem id ext)))
   ((file-exists-p (temp-problem id ext))
    (format "[[file:%s][?]]" (temp-problem id ext)))
   (t
    ;; Otherwise create a link for a new file
    (concat "[[elisp:(find-file \"" (temp-problem id ext) "\")][_]]"))))

(defun create-new (msg fname)
  "creates a new file inserting the text as comment"
  (progn 
    (find-file fname)
    ;; TODO: adding automatically commenting
    (insert msg)))

(defun temp-problem (id ext)
  (concat temp-dir
          (format prob-file id ext)))

(defun solved-problem (id ext)
  (concat 
   (format solved-dir id)
   (format prob-file id ext)))

(defun done ()
  "This function move the file when it's working"
  (interactive)
  (if (not buffer-file-name)
      (message "your file is not saved, save it before")
    (let*
        ((dir (concat "../" (sans-extension (file-name-nondirectory buffer-file-name))))
         (newfile (concat dir "/" (file-name-nondirectory buffer-file-name))))
      (if
          (yes-or-no-p "sure you solved the problem?")
          (progn
            (if (not (file-exists-p dir))
                (progn 
                  (message "creating directory for this problem")
                  (make-directory dir)))
            (rename-file buffer-file-name newfile)
            (kill-buffer))
        (message "yes check better your results first")))))

(defun sans-extension (fname)
  (substring fname 0 (string-match "\\." fname)))
