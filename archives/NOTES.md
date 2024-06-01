# NOTES

Deploying app in netify

5:19:51 PM: npm WARN EBADENGINE Unsupported engine {
5:19:51 PM: npm WARN EBADENGINE   package: 'aq-list-viz@1.0.0',
5:19:51 PM: npm WARN EBADENGINE   required: { npm: '2.4.x', node: '0.10.x' },
5:19:51 PM: npm WARN EBADENGINE   current: { node: 'v18.17.1', npm: '9.6.7' }
5:19:51 PM: npm WARN EBADENGINE }
5:19:51 PM: npm WARN deprecated request@2.12.0: request has been deprecated, see https://github.com/request/request/issues/3142

FIXED


5:30:19 PM: Failed during stage 'building site': Build script returned non-zero exit code: 2 (https://ntl.fyi/exit-code-2)
5:30:17 PM: Netlify Build                                                 
5:30:17 PM: ────────────────────────────────────────────────────────────────
5:30:17 PM: ​
5:30:17 PM: ❯ Version
5:30:17 PM:   @netlify/build 29.20.6
5:30:17 PM: ​
5:30:17 PM: ❯ Flags
5:30:17 PM:   baseRelDir: true
5:30:17 PM:   buildId: 64e1341fd46b3e052eea952a
5:30:17 PM:   deployId: 64e1341fd46b3e052eea952c
5:30:17 PM: ​
5:30:17 PM: ❯ Current directory
5:30:17 PM:   /opt/build/repo
5:30:17 PM: ​
5:30:17 PM: ❯ Config file
5:30:17 PM:   No config file was defined: using default values.
5:30:17 PM: ​
5:30:17 PM: ❯ Context
5:30:17 PM:   production
5:30:17 PM: ​
5:30:17 PM: Build command from Netlify app                                
5:30:17 PM: ────────────────────────────────────────────────────────────────
5:30:17 PM: ​
5:30:17 PM: $ gulp build
5:30:17 PM: [21:30:17] No gulpfile found
5:30:17 PM: ​
5:30:17 PM: build.command failed                                        
5:30:17 PM: ────────────────────────────────────────────────────────────────
5:30:17 PM: ​
5:30:17 PM:   Error message
5:30:17 PM:   Command failed with exit code 1: gulp build (https://ntl.fyi/exit-code-1)
5:30:17 PM: ​
5:30:17 PM:   Error location
5:30:17 PM:   In Build command from Netlify app:
5:30:17 PM:   gulp build
5:30:17 PM: ​
5:30:17 PM:   Resolved config
5:30:17 PM:   build:
5:30:17 PM:     command: gulp build
5:30:17 PM:     commandOrigin: ui
5:30:17 PM:     publish: /opt/build/repo/dist
5:30:17 PM:     publishOrigin: ui
5:30:19 PM: Build failed due to a user error: Build script returned non-zero exit code: 2
5:30:19 PM: Failing build: Failed to build site
5:30:19 PM: Finished processing build request in 29.091s
